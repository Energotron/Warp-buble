# Modified Gravity Research Watch

This directory is the durable research sink for the hourly ChatGPT automation **Modified Gravity Watch**.

The automation uses the installed skill `modified-gravity-research-watcher` as its governing research procedure. The repository integration does not redefine that skill's significance, source-quality, deduplication, classification, or reporting rules.

## Write policy

- Run hourly.
- If the skill significance threshold is **not** met: do not create a research commit.
- If the threshold **is** met: write a Markdown report into this directory and commit it to `main`.
- Before writing, search existing reports so the repository is also used as durable deduplication context.
- Preserve primary-source links, dates, classification, comparison with prior reported results, and relevance to warp / exotic-spacetime research when the skill requires them.

## Layout

- `INDEX.md` — compact chronological index of accepted significant reports.
- `reports/YYYY-MM-DD/` — timestamped research reports created only for significant developments.

## Automation

Scheduler: ChatGPT automation `Modified Gravity Watch`.
Cadence: hourly.
Target repository: `Energotron/Warp-buble` (`main`).
