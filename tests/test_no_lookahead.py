from src.positioning import equal_weight_positions


def test_positioning_uses_only_supplied_scores():
    earlier = {"MSFT": 2.0, "ABBV": 1.0}
    later = {"MSFT": 2.0, "ABBV": 1.0, "NVDA": 100.0}

    assert equal_weight_positions(earlier, 1) == {"MSFT": 1.0}
    assert equal_weight_positions(later, 1) == {"NVDA": 1.0}


def test_tied_scores_use_stable_symbol_order():
    assert equal_weight_positions(
        {"NVDA": 1.0, "ABBV": 1.0}, 1
    ) == {"ABBV": 1.0}

