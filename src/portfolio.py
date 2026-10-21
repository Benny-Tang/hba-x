"""Portfolio-weight validation and target-change utilities."""

from math import isfinite


def normalize_weights(weights: dict[str, float]) -> dict[str, float]:
    """Validate long-only weights; omit zero-weight positions."""
    result: dict[str, float] = {}
    for symbol, weight in weights.items():
        if not isinstance(symbol, str) or not symbol.strip():
            raise ValueError("Symbols must be non-empty strings")
        if isinstance(weight, bool) or not isinstance(weight, (int, float)):
            raise ValueError(f"Invalid weight for {symbol}")
        if not isfinite(weight) or weight < 0:
            raise ValueError(
                f"Weight for {symbol} must be finite and non-negative"
            )
        if weight > 0:
            result[symbol] = float(weight)

    if sum(result.values()) > 1.0 + 1e-9:
        raise ValueError("Total long-only portfolio weight cannot exceed 1.0")
    return result


def weight_changes(
    current: dict[str, float],
    target: dict[str, float],
) -> dict[str, float]:
    """Return target-minus-current changes, including full position closures."""
    current_valid = normalize_weights(current)
    target_valid = normalize_weights(target)
    symbols = set(current_valid) | set(target_valid)
    return {
        symbol: target_valid.get(symbol, 0.0) - current_valid.get(symbol, 0.0)
        for symbol in sorted(symbols)
        if abs(
            target_valid.get(symbol, 0.0) - current_valid.get(symbol, 0.0)
        ) > 1e-12
    }

