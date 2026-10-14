from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class Corporation:
    name: str
    sector: str
    influence: int
    stability: float
    regions: Tuple[str, ...] = ()


@dataclass
class GateNode:
    name: str
    region: str
    throughput: int
    status: str = "stable"
    latency_ms: int = 0


@dataclass
class NetworkTopology:
    corporations: List[Corporation]
    gates: Dict[str, GateNode]
    links: Dict[str, List[str]] = field(default_factory=dict)

    def connect(self, source: str, target: str) -> None:
        self.links.setdefault(source, [])
        self.links.setdefault(target, [])
        if target not in self.links[source]:
            self.links[source].append(target)
        if source not in self.links[target]:
            self.links[target].append(source)

    def route_cost(self, source: str, target: str) -> int:
        source_gate = self.gates[source]
        target_gate = self.gates[target]
        return abs(source_gate.throughput - target_gate.throughput) + abs(source_gate.latency_ms - target_gate.latency_ms)
