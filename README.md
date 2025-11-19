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

Throughout the testing process, several bugs and improvements were identified and fixed to achieve high coverage and reliable functionality.  
- **`apply_discount()`**: Fixed a logic error where percentages weren’t divided by 100, causing large incorrect discounts (e.g., `100 - 100*10 = -900`). It now correctly calculates `price - price*(percent/100)`.  
- **`parse_price()`**: Updated to properly validate and parse formatted prices like `"$1,234.50"` while rejecting malformed ones such as `"$12,34,56"`. This ensures correct handling of commas and currency symbols.  
- **`load_order()`**: Adjusted to split only on the first comma in each line, allowing prices containing commas to be parsed correctly.  
- **Tests**: Updated and expanded to reflect these fixes. Unit tests now cover normal and invalid inputs for all pricing functions, integration tests confirm end-to-end behavior with real files via `tmp_path`, and a regression test verifies that the original discount bug cannot reappear.  
- **Coverage**: Achieved ~96% overall test coverage, with only minor untested error-handling branches (e.g., malformed CSV detection).  

Together, these fixes ensure correctness, maintainability, and confidence in future code changes.
