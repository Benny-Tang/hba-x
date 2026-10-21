"""Small, explicit long-only portfolio risk controls."""

from src.portfolio import normalize_weights


def cap_weights(
    weights: dict[str, float],
    max_weight: float = 0.5,
) -> dict[str, float]:
    """Cap individual weights without redistributing the excess."""
    if isinstance(max_weight, bool) or not isinstance(max_weight, (int, float)):
        raise ValueError("max_weight must be numeric")
    if not 0 < max_weight <= 1:
        raise ValueError("max_weight must be in (0, 1]")

    validated = normalize_weights(weights)
    return {
        symbol: min(weight, float(max_weight))
        for symbol, weight in validated.items()
    }

