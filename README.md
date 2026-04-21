# KR3 Hunter

GitHub Actions pipeline for scouting games, fan projects, remakes, and spiritual successors inspired by **Space Rangers / Космические рейнджеры**.

## What it does
- searches GitHub repositories by RU/EN query packs
- enriches results with repository metadata
- scores candidates by similarity signals
- generates a Markdown report and JSON datasets
- uploads artifacts on every run

## Run
Use the **KR3 Similar Games Hunter** workflow from the Actions tab.

## Outputs
- `out/raw_candidates.json`
- `out/scored_candidates.json`
- `out/report.md`

## Notes
This pipeline is GitHub-centric by default. It can be extended later with external sources via scheduled crawlers or APIs.
