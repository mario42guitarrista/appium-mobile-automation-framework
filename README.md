# Mobile Automation Framework - Appium + Python

This repository contains a mobile automation framework built with Appium, Python, and Pytest.

---

## 🚀 Overview

This project simulates a banking application and demonstrates modern QA automation practices, including:

* Mobile automation using Appium
* Hybrid testing (API + UI validation)
* Data-driven testing
* Structured test architecture

The goal is to replicate real-world QA scenarios found in enterprise systems.

---

## 🏦 Banking Scenarios

The project covers realistic banking flows:

### Login

* Required fields validation
* Invalid credentials
* Successful login

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

---

## 🔁 Hybrid Testing (API + UI)

This project combines API and UI validation to improve reliability.

Examples:

* Login validated via API and UI
* Balance validated via API and UI
* Transaction history validated via API and UI

---

## 📊 Data-Driven Testing

Login scenarios are driven by external JSON data:

* Improves maintainability
* Allows easy expansion of test scenarios
* Separates test logic from test data

---

## 📜 Logging

The framework uses logging to improve visibility during test execution:

* Tracks test execution flow
* Helps debug failures
* Provides better traceability

---

## 📱 Mobile Automation

* Real interaction with Chrome on Android Emulator
* Appium + UiAutomator2
* Element validation and navigation

---

## 🏗️ Architecture

* Page Object Model (POM)
* Separation of concerns:

  * UI layer
  * API layer
  * Test layer
* Scalable and maintainable structure

---

## 📂 Project Structure

pages/      # Page Objects
tests/      # Test scenarios (smoke + banking + hybrid)
api/        # Simulated API layer
utils/      # Helpers and logging
data/       # Test data (JSON)
config/     # Capabilities and environment config

---

## ⚙️ Technologies

* Python
* Appium
* Pytest
* Android Emulator
* UiAutomator2

---

## ▶️ How to Run

```bash
pytest -v -s
```

---

## 🔥 Key Highlights

* Hybrid testing strategy (API + UI)
* Data-driven testing
* Logging for better traceability
* Real mobile automation with Appium
* Scalable test architecture

---

## 💼 Author

Mario Lima — QA Automation Engineer
