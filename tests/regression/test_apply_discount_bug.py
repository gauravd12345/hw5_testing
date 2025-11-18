import pytest
from src.pricing import apply_discount

def test_apply_discount_regression():
    """
    Regression test for the apply_discount() bug.

    Expected: percent should represent a percentage (e.g., 10 → 10%).
    Actual (buggy): function subtracts price * percent (not price * percent/100).
    """
    result = apply_discount(100.0, 10)
    # The correct discounted price should be 90.0
    assert result == pytest.approx(90.0)
