import re

_PRICE_RE = re.compile(
    r"""^\s*              # optional spaces
        \$?\s*            # optional $
        (?:               # integer part:
           \d{1,3}(?:,\d{3})*   # 1,234,567 style with proper comma groups
           | \d+                # or plain digits (no commas)
        )
        (?:\.\d+)?        # optional decimals
        \s*$              # optional spaces
    """,
    re.VERBOSE,
)

def parse_price(text):
    s = str(text)
    if not _PRICE_RE.match(s):
        raise ValueError(f"Invalid price: {text!r}")
    s = s.strip()
    if s.startswith("$"):
        s = s[1:].lstrip()
    s = s.replace(",", "")
    return float(s)

def format_currency(value):
    # Always 2 decimals, prefixed with $
    return "$" + f"{float(value):0.2f}"

def apply_discount(price, percent):
    """
    Reduce price by 'percent' (e.g., 10 means 10%).
    """
    if percent < 0:
        raise ValueError("percent must be >= 0")
    
    return price - price * (percent / 100)

def add_tax(price, rate=0.07):
    if rate < 0:
        raise ValueError("rate must be >= 0")
    return price * (1 + rate)

def bulk_total(prices, discount_percent=0, tax_rate=0.07):
    subtotal = 0.0
    for p in prices:
        subtotal += float(p)
    after_discount = apply_discount(subtotal, discount_percent)
    return add_tax(after_discount, tax_rate)
