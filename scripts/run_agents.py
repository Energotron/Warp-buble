#!/usr/bin/env python3
import base64
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.github.com"
TOKEN = os.getenv("GITHUB_TOKEN", "")
REPO = os.getenv("GITHUB_REPOSITORY", "")
PER_QUERY = int(os.getenv("PER_QUERY", "15"))
OUT = Path("out")
OUT.mkdir(exist_ok=True)


def headers(accept="application/vnd.github+json"):
    h = {
        "Accept": accept,
        "User-Agent": "kr3-hunter-action"
    }
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h


def gh_get(url):
    req = urllib.request.Request(url, headers=headers())
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read().decode("utf-8")
        return json.loads(data)


def search_repositories(query, per_page=20):
    encoded = urllib.parse.quote(query)
    url = f"{API}/search/repositories?q={encoded}&sort=updated&order=desc&per_page={per_page}"
    return gh_get(url).get("items", [])


def fetch_readme(full_name):
    url = f"{API}/repos/{full_name}/readme"
    try:
        data = gh_get(url)
        content = data.get("content", "")
        if data.get("encoding") == "base64" and content:
            return base64.b64decode(content).decode("utf-8", errors="ignore")
    except Exception:
        return ""
    return ""


def days_since(iso_dt):
    if not iso_dt:
        return 99999
    dt = datetime.strptime(iso_dt, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - dt).days


def normalize_repo(item):
    return {
        "id": item["id"],
        "full_name": item["full_name"],
        "html_url": item["html_url"],
        "description": item.get("description") or "",
        "topics": item.get("topics", []),
        "language": item.get("language"),
        "stargazers_count": item.get("stargazers_count", 0),
        "forks_count": item.get("forks_count", 0),
        "archived": item.get("archived", False),
        "updated_at": item.get("updated_at"),
        "pushed_at": item.get("pushed_at"),
        "default_branch": item.get("default_branch", "main"),
    }


def text_score(text, keywords, weight):
    text_low = (text or "").lower()
    hits = 0
    for kw in keywords:
        if kw in text_low:
            hits += 1
    return hits * weight, hits


def score_repo(repo, readme, cfg):
    weights = cfg["weights"]
    kws = cfg["keywords"]
    score = 0
    reasons = []

    name_s, name_hits = text_score(repo["full_name"], kws["core"], weights["name_match"])
    desc_s, desc_hits = text_score(repo["description"], kws["core"], weights["description_match"])
    readme_s, readme_hits = text_score(readme[:15000], kws["core"], weights["readme_match"])
    topics_s, topic_hits = text_score(" ".join(repo.get("topics", [])), kws["core"], weights["topic_match"])

    score += name_s + desc_s + readme_s + topics_s
    if name_hits:
        reasons.append(f"name:{name_hits}")
    if desc_hits:
        reasons.append(f"description:{desc_hits}")
    if readme_hits:
        reasons.append(f"readme:{readme_hits}")
    if topic_hits:
        reasons.append(f"topics:{topic_hits}")

    recency_days = min(days_since(repo.get("updated_at")), days_since(repo.get("pushed_at")))
    if recency_days <= 90:
        score += weights["recent_activity"]
        reasons.append("recent")
    elif recency_days <= 365:
        score += 1
        reasons.append("active-within-year")

    play_s, play_hits = text_score((repo["description"] + "\n" + readme)[:15000], kws["playability"], weights["playability_signals"])
    engine_s, engine_hits = text_score((repo["description"] + "\n" + readme)[:15000], kws["engine"], weights["engine_signal"])
    score += play_s + engine_s
    if play_hits:
        reasons.append(f"playability:{play_hits}")
    if engine_hits:
        reasons.append(f"engine:{engine_hits}")

    if repo.get("archived"):
        score += weights["archived_penalty"]
        reasons.append("archived")

    similarity_10 = round(max(0, min(10, score / 4)), 1)
    return score, similarity_10, reasons


def load_config():
    with open("config/queries.json", "r", encoding="utf-8") as f:
        return json.load(f)


def unique_by_full_name(items):
    seen = {}
    for item in items:
        seen[item["full_name"].lower()] = item
    return list(seen.values())


def write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def write_report(scored):
    lines = []
    lines.append("# KR3 Similar Games Hunter Report\n")
    lines.append(f"Generated at: {datetime.utcnow().isoformat()}Z\n")
    lines.append("\n## Top candidates\n")
    for idx, item in enumerate(scored[:20], start=1):
        lines.append(
            f"{idx}. **{item['full_name']}** — score `{item['score']}` / similarity `{item['similarity_10']}/10`  \n"
            f"   - URL: {item['html_url']}  \n"
            f"   - Updated: {item.get('updated_at','n/a')}  \n"
            f"   - Archived: {item.get('archived', False)}  \n"
            f"   - Description: {item.get('description','').strip() or '—'}  \n"
            f"   - Reasons: {', '.join(item.get('reasons', [])) or '—'}\n"
        )

    lines.append("\n## False positives / low-confidence\n")
    lows = [x for x in scored if x["similarity_10"] < 3][:10]
    if lows:
        for item in lows:
            lines.append(f"- {item['full_name']} — {item['similarity_10']}/10\n")
    else:
        lines.append("- None\n")

    with open(OUT / "report.md", "w", encoding="utf-8") as f:
        f.write("".join(lines))


def main():
    cfg = load_config()
    raw = []
    for query in cfg["queries"]:
        try:
            repos = search_repositories(query, per_page=PER_QUERY)
        except Exception as e:
            print(f"search failed for {query}: {e}", file=sys.stderr)
            continue
        for item in repos:
            raw.append(normalize_repo(item))
        time.sleep(1)

    unique = unique_by_full_name(raw)
    write_json(OUT / "raw_candidates.json", unique)

    scored = []
    for repo in unique:
        readme = fetch_readme(repo["full_name"])
        score, similarity_10, reasons = score_repo(repo, readme, cfg)
        repo = dict(repo)
        repo["readme_excerpt"] = re.sub(r"\s+", " ", readme[:500]).strip()
        repo["score"] = score
        repo["similarity_10"] = similarity_10
        repo["reasons"] = reasons
        scored.append(repo)
        time.sleep(0.4)

    scored.sort(key=lambda x: (x["score"], x["stargazers_count"], x["forks_count"]), reverse=True)
    write_json(OUT / "scored_candidates.json", scored)
    write_report(scored)

    summary = [
        "## KR3 Hunter Summary",
        "",
        f"Candidates found: **{len(unique)}**",
        f"Scored candidates: **{len(scored)}**",
        "",
        "### Top 5",
    ]
    for item in scored[:5]:
        summary.append(f"- {item['full_name']} — {item['similarity_10']}/10")

    summary_text = "\n".join(summary) + "\n"
    print(summary_text)
    summary_file = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a", encoding="utf-8") as f:
            f.write(summary_text)


if __name__ == "__main__":
    main()
