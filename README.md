# Mobile Automation Framework - Appium + Python

This repository contains a mobile automation framework built with Appium, Python, and Pytest.

---

## Overview

This project simulates a banking application and demonstrates modern QA automation practices, including:

* Mobile automation using Appium
* Hybrid testing (API + UI validation)
* Data-driven testing
* Logging for test traceability
* Full flow validation
* AI-inspired validation for more resilient assertions

The goal is to simulate real-world QA scenarios found in enterprise systems.

---

## Banking Scenarios

The project covers realistic banking flows:

### Login

* Required fields validation
* Invalid credentials
* Successful login
* Data-driven login scenarios using JSON

### Balance

* Balance visibility
* Balance validation

### Transfer

* Successful transfer
* Insufficient balance
* Invalid amount

### Transaction History

* History availability
* Transfer presence validation

### Full Flow

* Login → Balance → Transfer → Validation

---

## Hybrid Testing (API + UI)

This project combines API and UI validation to improve reliability and simulate real QA strategies.

Examples:

* Login validated via API and UI
* Balance validated via API and UI
* Transaction history validated via API and UI

---

## Data-Driven Testing

Login scenarios are driven by external JSON data.

Benefits:

* easier maintenance
* easier expansion of test cases
* separation between test logic and test data

---

## Logging

The framework uses logging to improve visibility during execution.

Benefits:

* tracks test execution flow
* improves debugging
* provides better traceability

---

## AI-Based Validation

The framework includes an AI-inspired validation layer to reduce brittle assertions.

Instead of relying only on a single fixed success message, the project validates transfer messages semantically using keyword-based intelligent checks.

Benefits:

* reduces false negatives
* improves resilience of assertions
* better reflects real-world message variations

---

## Mobile Automation

* Real interaction with Chrome on Android Emulator
* Appium + UiAutomator2
* Element validation and navigation

---

## Architecture

* Page Object Model (POM)
* Separation of concerns:

  * UI layer
  * API layer
  * Test layer
  * Test data layer
  * Utility layer
* Scalable and maintainable structure

---

## Project Structure

pages/      # Page Objects
tests/      # Test scenarios (smoke + banking + hybrid + full flow)
api/        # Simulated API layer
utils/      # Helpers, logger, AI-inspired validator
data/       # Test data (JSON)
config/     # Capabilities and environment config

---

## Technologies

* Python
* Appium
* Pytest
* Android Emulator
* UiAutomator2

---

## How to Run

```bash
pytest -v -s
```

---

## Key Highlights

* Hybrid testing strategy (API + UI)
* Data-driven testing
* Logging for better traceability
* Full flow business validation
* AI-inspired semantic assertion strategy
* Real mobile automation with Appium
* Scalable test architecture

## QA Failure Analyzer Agent

The project includes a QA Failure Analyzer Agent designed to classify common automation failures and support faster triage.

### Covered categories
- stale element reference
- locator/timing issues
- timeout failures
- assertion failures

### Features
- failure categorization
- probable cause suggestion
- remediation guidance
- formatted failure report
- realistic stacktrace analysis
- execution logging

### Benefits
- faster debugging
- more efficient failure triage
- improved maintainability of automation suites

## CI / GitHub Actions

This project includes a GitHub Actions workflow to automatically run non-mobile test suites on every push and pull request.

Covered in CI:
- banking scenarios
- hybrid validations
- QA Failure Analyzer Agent

This helps ensure continuous validation and improves project reliability.
---

## Author

Mario Lima — QA Automation Engineer
