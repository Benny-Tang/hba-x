import pytest

from src.portfolio import normalize_weights
from src.positioning import equal_weight_positions
from src.risk_controls import cap_weights


def test_weights_cannot_exceed_total_capital():
    with pytest.raises(ValueError):
        normalize_weights({"MSFT": 0.7, "ABBV": 0.4})


def test_negative_weight_rejected():
    with pytest.raises(ValueError):
        normalize_weights({"MSFT": -0.1})


def test_position_cap_applied():
    assert cap_weights({"MSFT": 0.8, "ABBV": 0.2}, 0.5) == {
        "MSFT": 0.5,
        "ABBV": 0.2,
    }


def test_equal_weight_selection_is_deterministic():
    assert equal_weight_positions(
        {"ABBV": 2, "MSFT": 5, "NVDA": 4}, 2
    ) == {"MSFT": 0.5, "NVDA": 0.5}


def test_empty_scores_produce_cash():
    assert equal_weight_positions({}, 2) == {}


def test_invalid_position_count_rejected():
    with pytest.raises(ValueError):
        equal_weight_positions({"MSFT": 1.0}, 0)

