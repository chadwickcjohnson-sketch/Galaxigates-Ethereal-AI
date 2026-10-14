# Galaxy Gate Corporations & Networks

A compact Python project for modeling the strategic trade, logistics, and relay behavior of the Galaxy Gate network.

The repository contains a resilient, testable simulation of interstellar corporations, gate hubs, and route analysis for the Ethereal AI command lattice.

## Project goals

- Model major corporations operating between star systems
- Map gate relays, network throughput, and system health
- Analyze routing and corridor stability across the network
- Provide a clean, testable foundation for future AI-driven strategic planning

## Quick start

```bash
python -m pip install -e .
python -m galaxigates_ethereal_ai
```

To inspect route optimization:

```bash
python main.py --from Helios --to Vespera
```

## Included modules

- `galaxigates_ethereal_ai/models.py` — corporate and network data structures
- `galaxigates_ethereal_ai/engine.py` — route generation and network analysis
- `main.py` — command-line entry point for quick exploration
- `tests/test_network.py` — unit coverage for core behavior

## Example output

```text
Galaxy Gate Network Summary
  Corporations: 4
  Gate nodes: 6
  Mean stability: 0.87
  Best route: Helios -> Asterion -> Vespera
```
