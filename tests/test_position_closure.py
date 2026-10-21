from src.portfolio import weight_changes


def test_dropped_position_gets_full_closure():
    changes = weight_changes(
        {"MSFT": 0.5, "ABBV": 0.5},
        {"MSFT": 1.0},
    )
    assert changes == {"ABBV": -0.5, "MSFT": 0.5}


def test_omitted_position_means_zero_not_carry_forward():
    assert weight_changes({"ABBV": 0.4}, {}) == {"ABBV": -0.4}


def test_unchanged_weights_have_no_trade():
    assert weight_changes({"MSFT": 0.5}, {"MSFT": 0.5}) == {}


def test_zero_target_closes_position():
    assert weight_changes({"ABBV": 0.4}, {"ABBV": 0.0}) == {
        "ABBV": -0.4
    }

