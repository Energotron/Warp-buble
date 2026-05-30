from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
import json
from typing import Any


@dataclass
class MissionState:
    generated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    mission_brief: str = ""
    priorities: list[str] = field(default_factory=list)
    blockers: list[str] = field(default_factory=list)
    actions: list[str] = field(default_factory=list)
    artifacts: dict[str, Any] = field(default_factory=dict)


class StateStore:
    def __init__(self, root: str | Path = ".state") -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.path = self.root / "mission_state.json"

    def load(self) -> MissionState:
        if not self.path.exists():
            return MissionState()
        data = json.loads(self.path.read_text(encoding="utf-8"))
        return MissionState(**data)

    def save(self, state: MissionState) -> None:
        self.path.write_text(json.dumps(asdict(state), ensure_ascii=False, indent=2), encoding="utf-8")
