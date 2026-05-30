from __future__ import annotations

import argparse
import os
from pathlib import Path

from .agents import (
    ArchivistAgent,
    AnalystAgent,
    BaseAgent,
    BuilderAgent,
    CommsAgent,
    CommandAgent,
    FundingAgent,
    PMAgent,
    RiskAgent,
    ScoutAgent,
)
from .state import MissionState, StateStore


def build_agents() -> list[BaseAgent]:
    return [
        ScoutAgent("Scout Agent", "Scan for relevant research and signals."),
        ArchivistAgent("Archivist Agent", "Store and link knowledge artifacts."),
        AnalystAgent("Analyst Agent", "Assess quality, novelty, and feasibility."),
        RiskAgent("Risk Agent", "Flag weak claims and logical gaps."),
        PMAgent("PM Agent", "Translate findings into tasks and milestones."),
        BuilderAgent("Builder Agent", "Draft code, simulations, and automation."),
        CommsAgent("Comms Agent", "Prepare outreach and updates."),
        FundingAgent("Funding Agent", "Track grants, donors, and opportunities."),
        CommandAgent("Command Agent", "Coordinate the mission cycle."),
    ]


def run_cycle(state: MissionState) -> MissionState:
    for agent in build_agents():
        state = agent.run(state)
    return state


def main() -> int:
    parser = argparse.ArgumentParser(description="QuantDeus Mission OS")
    parser.add_argument("--once", action="store_true", help="Run one mission cycle and exit")
    parser.add_argument("--state-dir", default=os.getenv("MISSION_OS_STATE_DIR", ".state"))
    args = parser.parse_args()

    store = StateStore(Path(args.state_dir))
    state = store.load()
    state = run_cycle(state)
    store.save(state)

    print("QuantDeus Mission OS cycle complete")
    print(state.mission_brief)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
