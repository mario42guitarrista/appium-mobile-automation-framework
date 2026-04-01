# 📱 Mobile Banking QA Automation Platform

**Appium | Python | Pytest | AI-driven Testing | Docker**

---

## 🚀 Overview

End-to-end QA automation platform simulating a real-world mobile banking system.

This project goes beyond traditional test automation by combining:

* Mobile automation
* API validation
* AI-assisted failure analysis
* CI/CD integration
* Dockerized backend environment

It was designed to reflect real QA challenges found in modern distributed systems.

---

## 🧠 Key Highlights

* 📲 Mobile automation with Appium (Android Emulator)
* 🔄 End-to-end business flows (login → transfer → validation)
* 🔗 Hybrid testing strategy (API + UI validation)
* 📊 Data-driven testing (JSON-based scenarios)
* 🧾 Structured logging for traceability
* 🤖 AI-powered failure analysis (custom Failure Analyzer)
* 📁 Automatic failure report generation (JSON)
* ⚙️ CI/CD with GitHub Actions
* 🐳 Dockerized mock API for controlled testing environment

---

## 🏦 Business Scenarios Covered

### Authentication

* Required fields validation
* Invalid credentials
* Successful login
* Data-driven scenarios

### Balance

* Balance validation via API and UI

### Transfer

* Successful transfer
* Insufficient balance
* Invalid amount

### Transaction History

* History validation
* Transfer verification

### Full Flow

* Login → Balance → Transfer → Validation

---

## 🔗 Hybrid Testing (API + UI)

This project combines API and UI validation to reduce flakiness and improve confidence.

Examples:

* Login validated via API and UI
* Balance validated via API and UI
* Transfer validated via API + business rules

---

## 🤖 AI Failure Analyzer

A custom-built failure analysis module integrated into the test execution lifecycle.

### Features

* Failure classification (timeout, locator issues, stale elements, assertions)
* Probable root cause detection
* Suggested corrective actions
* Automatic execution on test failure
* JSON report generation for each failure

### Example Output

```json
{
  "error_type": "AssertionFailure",
  "possible_cause": "Validation did not match expected result",
  "suggestion": "Review expected vs actual outcome"
}
```

---

## 📊 Failure Reporting

On test failure, the framework automatically:

* captures screenshots
* analyzes failure using AI logic
* generates structured JSON reports

Location:

```bash
reports/failure_analysis/
```

---

## 🧠 AI-Inspired Validation

Implements semantic validation strategies to reduce brittle assertions.

Instead of relying only on exact strings, the framework validates outcomes using intelligent logic.

---

## 🏗️ Architecture

* Page Object Model (POM)
* Modular structure
* Domain separation:

  * `banking`
  * `qa_agent`
  * `smoke`

### Layers

* `pages/` → UI abstraction
* `tests/` → Test scenarios
* `api/` → API integration layer
* `utils/` → Helpers and infrastructure
* `ai/` → Failure analysis engine
* `config/` → Environment configuration
* `data/` → Test data

---

## 📁 Project Structure

```bash
pages/
tests/
api/
utils/
ai/
config/
data/
mock_api/
.github/workflows/
```

---

## 🐳 Mock API (Docker)

A fully functional mock banking API is included to simulate backend behavior.

### Run with Docker

```bash
docker compose up --build
```

### Base URL

```
http://127.0.0.1:5000
```

### Available Endpoints

* `POST /login`
* `GET /balance/<username>`
* `POST /transfer`
* `GET /history/<username>`

---

## ⚙️ CI/CD (GitHub Actions)

Automated test execution on:

* push
* pull request

Includes:

* QA Agent tests
* Failure analysis artifact upload
* Screenshot artifact upload

---

## ▶️ Running Tests

### Run all tests

```bash
pytest -v -s
```

### Run non-mobile tests

```bash
pytest tests/qa_agent -v -s
```

---

## 💡 Why This Project

This project was designed to simulate real-world QA engineering challenges:

* scalable automation architecture
* hybrid testing strategy
* intelligent failure analysis
* reproducible environments (Docker)
* CI/CD integration

---

## 👨‍💻 Author

Mario Lima
QA Automation Engineer focused on modern test architecture, AI-driven testing, and scalable QA solutions.
