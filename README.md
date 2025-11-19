# Homework 5
- Name: Gaurav Dharmadhikari
  
## Question 1
  Unit test - Tests one small part of the code (like a single function) to make sure it works right. It is used when checking individual pieces of code during development.
  Integration test - Tests how different parts of the program work together. It is used when making sure combined modules or systems interact correctly.
  Regression test - Tests old features to make sure new changes didn’t break them. It is used after updates or bug fixes.

## Question 2

Pytest discovery - Pytest finds tests in files named `test_*.py` or `*_test.py`, and runs functions that start with `test_`.
Fixture - A fixture is a setup helper that provides data or resources a test needs. It’s made with `@pytest.fixture` and passed into test functions.


## Summary of Fixes and Changes

During testing, several bugs were found and fixed to make the program work correctly and increase coverage.  
- **`apply_discount()`**: Fixed a bug where the percentage was not divided by 100. It now correctly calculates discounts like 10% off 100 = 90.  
- **`parse_price()`**: Updated to accept valid prices like `"$1,234.50"` and reject bad ones like `"$12,34,56"`.  
- **`load_order()`**: Changed to split only on the first comma so prices with commas work correctly.  
- **Tests**: Added and updated unit, integration, and regression tests. All main functions are now tested.  
- **Coverage**: Reached about 96% total coverage, with only a few untested error cases (e.g., malformed file lines).  


## Pytest Features Used

- **`@pytest.mark.parametrize`** – used to test many inputs in one test (e.g., different price formats).  
- **Fixtures** – used to share setup across tests.  
  - `sample_prices`: simple fixture for price lists.  
  - `tmp_path`: built-in fixture for making temp files in integration tests.  
- **`pytest.approx`** – used to compare floating-point numbers like totals.  
- **Regression test** – added a test to make sure the old `apply_discount()` bug never comes back.  

These pytest features helped make the tests cleaner, reusable, and more reliable.

