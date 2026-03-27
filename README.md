# Mobile Automation Framework - Appium + Python

This repository contains a mobile automation framework built with Appium, Python, and Pytest.

## Tech Stack
- Python
- Appium
- Pytest
- Android Emulator
- UiAutomator2

## Current Scope
- Real mobile automation using Chrome on Android Emulator
- Page Object Model (POM)
- Hybrid testing (API + UI validation)
- Banking domain simulation
- Pytest-based execution

## Project Structure
- `pages/` – Page Objects
- `tests/` – Test scenarios (smoke + banking + hybrid)
- `api/` – Simulated API layer for hybrid testing
- `utils/` – Driver and helper utilities
- `config/` – Capabilities and environment config

## Test Coverage

### Banking Scenarios
- Login validation (required fields, invalid credentials, success)
- Balance validation
- Transfer scenarios:
  - success
  - insufficient balance
  - invalid amount
- Transaction history validation

### Hybrid Testing (API + UI)
- Login validation via API + UI
- Balance validation via API + UI
- Transaction history validation via API + UI

### Mobile Automation
- Real interaction with Chrome using Appium

## How to Run

```bash
pytest -v -s