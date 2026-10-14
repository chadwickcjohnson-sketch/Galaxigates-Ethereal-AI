from __future__ import annotations

from collections import deque
from typing import Dict, Iterable, List, Tuple

from .models import Corporation, GateNode, NetworkTopology


def build_default_network() -> NetworkTopology:
    corporations = [
        Corporation("Helios Commerce Guild", "Trade", 92, 0.91, ("Aurelia", "Helios")),
        Corporation("Asterion Logistics", "Logistics", 88, 0.87, ("Asterion", "Vespera")),
        Corporation("Nocturne Ops", "Security", 81, 0.82, ("Nyx", "Cassiopeia")),
        Corporation("Ethereal Relay Syndicate", "Energy", 96, 0.94, ("Lumen", "Elyra")),
    ]

    gates = {
        "Helios": GateNode("Helios", "Helios", 120, "stable", 18),
        "Asterion": GateNode("Asterion", "Asterion", 95, "stable", 24),
        "Vespera": GateNode("Vespera", "Vespera", 108, "stable", 20),
        "Nyx": GateNode("Nyx", "Nyx", 88, "watch", 35),
        "Cassiopeia": GateNode("Cassiopeia", "Cassiopeia", 130, "stable", 16),
        "Lumen": GateNode("Lumen", "Lumen", 100, "stable", 22),
        "Elyra": GateNode("Elyra", "Elyra", 114, "stable", 19),
    }

    network = NetworkTopology(corporations, gates)
    links = {
        "Helios": ["Asterion", "Lumen"],
        "Asterion": ["Helios", "Vespera", "Nyx"],
        "Vespera": ["Asterion", "Cassiopeia"],
        "Nyx": ["Asterion", "Cassiopeia"],
        "Cassiopeia": ["Vespera", "Nyx", "Elyra"],
        "Lumen": ["Helios", "Elyra"],
        "Elyra": ["Lumen", "Cassiopeia"],
    }
    for source, destinations in links.items():
        for destination in destinations:
            network.connect(source, destination)

    return network


def summarize_network(network: NetworkTopology) -> Dict[str, float | int | str]:
    total_throughput = sum(gate.throughput for gate in network.gates.values())
    mean_stability = sum(corp.stability for corp in network.corporations) / len(network.corporations)
    active_gate_count = sum(1 for gate in network.gates.values() if gate.status == "stable")
    return {
        "corporations": len(network.corporations),
        "gate_nodes": len(network.gates),
        "total_throughput": total_throughput,
        "mean_stability": round(mean_stability, 2),
        "stable_gate_nodes": active_gate_count,
    }


def shortest_path(network: NetworkTopology, source: str, target: str) -> List[str]:
    if source == target:
        return [source]
    if source not in network.gates or target not in network.gates:
        raise ValueError(f"Unknown gate nodes: {source!r} or {target!r}")

    queue: deque[Tuple[str, List[str]]] = deque([(source, [source])])
    visited = {source}

    while queue:
        current, path = queue.popleft()
        for neighbor in network.links.get(current, []):
            if neighbor in visited:
                continue
            next_path = path + [neighbor]
            if neighbor == target:
                return next_path
            visited.add(neighbor)
            queue.append((neighbor, next_path))

    raise ValueError(f"No route exists from {source} to {target}")


def route_score(network: NetworkTopology, path: Iterable[str]) -> int:
    steps = list(path)
    total = 0
    for left, right in zip(steps, steps[1:]):
        total += network.route_cost(left, right)
    return total
