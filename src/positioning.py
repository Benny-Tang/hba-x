"""Simple deterministic placeholder for testing the HBA-X interface.

This is not the HBA strategy or a validated alpha model.
"""

from src.portfolio import normalize_weights


def equal_weight_positions(
    scores: dict[str, float],
    max_positions: int = 2,
) -> dict[str, float]:
    """Select the highest positive scores and assign equal long-only weights."""
    if isinstance(max_positions, bool) or not isinstance(max_positions, int):
        raise ValueError("max_positions must be an integer")
    if max_positions < 1:
        raise ValueError("max_positions must be at least 1")

    eligible: list[tuple[str, float]] = []
    for symbol, score in scores.items():
        if not isinstance(symbol, str) or not symbol.strip():
            raise ValueError("Symbols must be non-empty strings")
        if isinstance(score, bool) or not isinstance(score, (int, float)):
            continue
        if score > 0:
            eligible.append((symbol, float(score)))

    selected = sorted(eligible, key=lambda item: (-item[1], item[0]))[
        :max_positions
    ]
    if not selected:
        return {}

    weight = 1.0 / len(selected)
    return normalize_weights({symbol: weight for symbol, _ in selected})

