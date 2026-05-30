# QuantDeus Mission OS

A lightweight multi-agent command layer for research scouting, knowledge capture, analysis, project management, outreach, and funding coordination.

## What is included
- `src/quantdeus/`: runnable Python package
- `prompts/`: prompt templates for each agent
- `.github/workflows/mission-os.yml`: scheduled orchestration stub
- `QuantDeus_Mission_OS.md`: strategy/spec document

## Local run
```bash
python -m quantdeus.main --once
```

## Environment variables
- `OPENAI_API_KEY` or any provider-specific key you wire in
- `MISSION_OS_MODE=mock|live`
- `MISSION_OS_STATE_DIR=.state`

## Notes
This repo is intentionally structured as a deployable scaffold. Replace the mock LLM adapter with your preferred provider, then connect schedulers, storage, and notification channels.
