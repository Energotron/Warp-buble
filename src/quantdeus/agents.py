from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .state import MissionState


class Agent(Protocol):
    name: str

    def run(self, state: MissionState) -> MissionState: ...


@dataclass
class BaseAgent:
    name: str
    instruction: str

    def run(self, state: MissionState) -> MissionState:
        # Minimal deterministic scaffold until a live LLM/tool layer is wired in.
        state.artifacts[self.name] = {
            "instruction": self.instruction,
            "status": "prepared",
        }
        return state


class CommandAgent(BaseAgent):
    def run(self, state: MissionState) -> MissionState:
        state.mission_brief = "QuantDeus mission cycle executed."
        state.priorities = [
            "Track advanced propulsion research",
            "Capture and link knowledge",
            "Convert findings into action items",
        ]
        state.blockers = ["No live data connectors configured yet"]
        state.actions = [
            "Review incoming research",
            "Assign next experiments",
            "Prepare outreach targets",
        ]
        state.artifacts[self.name] = {"status": "commanded"}
        return state


class ScoutAgent(BaseAgent):
    pass


class ArchivistAgent(BaseAgent):
    pass


class AnalystAgent(BaseAgent):
    pass


class PMAgent(BaseAgent):
    pass


class RiskAgent(BaseAgent):
    pass


class BuilderAgent(BaseAgent):
    pass


class CommsAgent(BaseAgent):
    pass


class FundingAgent(BaseAgent):
    pass
