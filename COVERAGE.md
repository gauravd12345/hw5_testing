# COVERAGE REPORT

# Results:

| File            | Statements   | Miss        | Coverage      | Missing Lines |
| --------------- | ------------ | ----------- | ------------- | ------------- |
| src/order_io.py | 20           | 2           | 90%           | 8, 11         |
| src/pricing.py  | 27           | 0           | 100%          |               |
| **TOTAL** | **47** | **2** | **96%** |               |

**Total coverage:** 96%

**All 21 tests passed successfully.**

---

## Uncovered Lines / Functions

* **src/order_io.py: lines 8 and 11**

  These lines belong to the part of `load_order()` that raises a `ValueError` when a malformed CSV line is encountered.

---

## Analysis

* The uncovered lines are  **error-handling code** , only triggered when the input file format is invalid.
* Since the integration tests focus on valid file processing, this untested path is acceptable for typical usage.
* To achieve 100% coverage, a small additional test could be added to confirm that malformed input raises `ValueError`.

---

## Conclusion

* Current test coverage is excellent (96%).
* All key components (`parse_price`, `format_currency`, `apply_discount`, `add_tax`, `bulk_total`, and I/O integration) are fully tested.
* Only defensive error-handling branches remain untested.
