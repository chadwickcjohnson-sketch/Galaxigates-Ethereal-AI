from __future__ import annotations

import argparse
import json
from typing import Any

from galaxigates_ethereal_ai.engine import build_default_network, route_score, shortest_path, summarize_network


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Galaxy Gate Corporations & Networks simulator")
    parser.add_argument("--from", dest="source", default="Helios", help="Origin gate node")
    parser.add_argument("--to", dest="target", default="Vespera", help="Destination gate node")
    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    network = build_default_network()
    summary = summarize_network(network)
    route = shortest_path(network, args.source, args.target)
    best_path = route
    best_score = route_score(network, best_path)

    payload = {
        "title": "Galaxy Gate Network Summary",
        "summary": summary,
        "route": {
            "from": args.source,
            "to": args.target,
            "path": best_path,
            "score": best_score,
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
