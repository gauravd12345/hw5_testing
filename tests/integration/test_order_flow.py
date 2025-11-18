import pytest
from src.order_io import load_order, write_receipt
from src.pricing import bulk_total, format_currency

def test_order_integration_basic(tmp_path):
    # 1) Create a small CSV input
    input_file = tmp_path / "order.csv"
    input_file.write_text("widget,$10.00\ngizmo,5.50\n", encoding="utf-8")

    # 2) Load items and compute total
    items = load_order(input_file)
    prices = [p for (_n, p) in items]
    discount_percent = 0           # avoid coupling to apply_discount bug
    tax_rate = 0.07
    expected_total = bulk_total(prices, discount_percent, tax_rate)

    # 3) Write receipt
    receipt_path = tmp_path / "receipt.txt"
    write_receipt(receipt_path, items, discount_percent, tax_rate)

    # 4) Verify output
    output_text = receipt_path.read_text(encoding="utf-8")
    # item lines present
    assert "widget: $10.00" in output_text
    assert "gizmo: $5.50" in output_text
    # correctly formatted TOTAL line (use library’s own formatter for expected)
    assert f"TOTAL: {format_currency(expected_total)}" in output_text


@pytest.mark.parametrize(
    "csv_text,discount_percent,tax_rate",
    [
        ("thing,$1,234.50\npart, 0.50\n", 0, 0.10),  # commas, spaces, custom tax
        ("alpha,12.5\nbeta, $0.99 \n", 0, 0.07),     # bare number + spaced $ value
    ],
)
def test_order_integration_varied_inputs(tmp_path, csv_text, discount_percent, tax_rate):
    input_file = tmp_path / "order.csv"
    input_file.write_text(csv_text, encoding="utf-8")

    items = load_order(input_file)
    prices = [p for (_n, p) in items]

    expected_total = bulk_total(prices, discount_percent, tax_rate)

    receipt_path = tmp_path / "receipt.txt"
    write_receipt(receipt_path, items, discount_percent, tax_rate)

    out = receipt_path.read_text(encoding="utf-8")

    # Every item should appear as "<name>: $x.yy"
    for name, price in items:
        assert f"{name}: {format_currency(price)}" in out

    assert f"TOTAL: {format_currency(expected_total)}" in out
