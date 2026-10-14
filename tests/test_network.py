from .engine import build_default_network, route_score, shortest_path, summarize_network


def main() -> None:
    network = build_default_network()
    summary = summarize_network(network)
    route = shortest_path(network, "Helios", "Vespera")
    print("Galaxy Gate Network Summary")
    print(f"  Corporations: {summary['corporations']}")
    print(f"  Gate nodes: {summary['gate_nodes']}")
    print(f"  Mean stability: {summary['mean_stability']:.2f}")
    print(f"  Best route: {' -> '.join(route)}")
    print(f"  Route cost: {route_score(network, route)}")


if __name__ == "__main__":
    main()
