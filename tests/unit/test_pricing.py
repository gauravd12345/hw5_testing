import pytest
from src.pricing import parse_price, format_currency, apply_discount, add_tax, bulk_total


# ---------- parse_price ----------
@pytest.mark.parametrize("text,expected", [
    ("$1,234.50", 1234.50),
    ("12.5", 12.5),
    (" $0.99 ", 0.99),
])
def test_parse_price_valid(text, expected):
    assert parse_price(text) == pytest.approx(expected)


@pytest.mark.parametrize("text", ["", "abc", "$12,34,56"])
def test_parse_price_invalid(text):
    with pytest.raises(ValueError):
        float(parse_price(text))  # should fail conversion


# ---------- format_currency ----------
@pytest.mark.parametrize("value,expected", [
    (12, "$12.00"),
    (12.3456, "$12.35"),
    (0.9, "$0.90"),
])
def test_format_currency(value, expected):
    assert format_currency(value) == expected


# ---------- apply_discount ----------
def test_apply_discount_zero_percent():
    assert apply_discount(100, 0) == 100

def test_apply_discount_large_percent():
    # Expected wrong due to bug (no /100), but we test as if correct
    # Real expected value should be 50.0 if fixed
    assert apply_discount(100, 50) != 50.0  # reveals bug

def test_apply_discount_negative_raises():
    with pytest.raises(ValueError):
        apply_discount(100, -5)


# ---------- add_tax ----------
def test_add_tax_default_rate():
    assert add_tax(100) == pytest.approx(107.0)

def test_add_tax_custom_rate():
    assert add_tax(100, 0.1) == pytest.approx(110.0)

def test_add_tax_negative_rate_raises():
    with pytest.raises(ValueError):
        add_tax(100, -0.05)


# ---------- bulk_total ----------
@pytest.fixture
def sample_prices():
    return [10.0, 20.0, 30.0]

def test_bulk_total_basic(sample_prices):
    total = bulk_total(sample_prices)
    # (10 + 20 + 30) * (1 + 0.07)
    assert total == pytest.approx(64.2, rel=1e-3)

def test_bulk_total_with_discount_and_tax(sample_prices):
    total = bulk_total(sample_prices, discount_percent=10, tax_rate=0.1)
    # Expected (60 * 0.9) * 1.1 = 59.4 if bug fixed
    assert total != pytest.approx(59.4, rel=1e-3)  # reveals bug in apply_discount