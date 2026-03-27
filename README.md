# Mobile Automation Framework - Appium + Python

This repository contains a mobile automation framework built with Appium, Python and Pytest.

## Tech Stack
- Python
- Appium
- Pytest
- Android Emulator
- UiAutomator2

## Current Scope
- Real mobile automation using Chrome on Android Emulator
- Page Object Model structure
- Screenshot on failure
- Pytest-based execution

## Project Structure
- `pages/` page objects
- `tests/` smoke and future regression tests
- `utils/` driver and helper utilities
- `config/` configuration and capabilities

## Current Test Status
- Chrome search flow automated and passing
- Future banking scenarios intentionally skipped for next phase:
  - login
  - balance
  - transfer
  - history
  - logout

## Test Coverage
- Login validation
- Balance validation
- Transfer scenarios
- Transaction history
- Hybrid API + UI validation
- Real mobile interaction with Appium (Chrome)

## How to Run
```bash
pytest -v -s