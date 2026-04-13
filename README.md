# 🚀 Mobile Banking QA Automation Platform (Hybrid + AI + Observability)

Appium | Python | Pytest | AI-driven Testing | Docker

---

## 🚀 Overview

End-to-end QA automation platform simulating a real-world mobile banking system.

This project goes beyond traditional test automation by combining:

- Mobile automation  
- API validation  
- AI-assisted failure analysis  
- CI/CD integration  
- Dockerized backend environment  

It was designed to reflect real QA challenges found in modern distributed systems.

---

## 🧠 Key Highlights

📲 Mobile automation with Appium (Android Emulator)  
🔄 End-to-end business flows (login → transfer → validation)  
🔗 Hybrid testing strategy (API + UI validation)  
📊 Data-driven testing (JSON-based scenarios)  
🧾 Structured logging for traceability  
🤖 AI-powered failure analysis (custom Failure Analyzer)  
📁 Automatic failure report generation (JSON)  
⚙️ CI/CD with GitHub Actions  
🐳 Dockerized mock API for controlled testing environment  

---

## ⚙️ Robust API Layer

- Timeout handling  
- Safe JSON parsing (handles non-JSON responses)  
- Structured error handling (connection errors, timeouts)  
- Consistent response format across all endpoints  

---

## 🏷️ Test Tagging (Pytest)

- Smoke tests  
- Regression tests  
- API tests  
- Mobile tests  
- Hybrid tests  

Example commands:

    pytest -m smoke -v
    pytest -m hybrid -v
    pytest -m api -v

---

## 📊 Execution Observability

- Structured execution logs  
- Execution summary reports  
- HTML dashboard  

Dashboard location:

    reports/execution_logs/dashboard.html

---

## 🏦 Business Scenarios Covered

### Authentication
- Required fields validation  
- Invalid credentials  
- Successful login  
- Data-driven scenarios  

### Balance
- Balance validation via API and UI  

### Transfer
- Successful transfer  
- Insufficient balance  
- Invalid amount  

### Transaction History
- History validation  
- Transfer verification  

### Full Flow
- Login → Balance → Transfer → Validation  

---

## 🔗 Hybrid Testing (API + UI)

This project combines API and UI validation to reduce flakiness and improve confidence.

Examples:

- Login validated via API and UI  
- Balance validated via API and UI  
- Transfer validated via API + business rules  

---

## 🤖 AI Failure Analyzer

A custom-built failure analysis module integrated into the test execution lifecycle.

### Features

- Failure classification (timeout, locator issues, stale elements, assertions)  
- Probable root cause detection  
- Suggested corrective actions  
- Automatic execution on test failure  
- JSON report generation for each failure  

Example output:

{
  "error_type": "AssertionFailure",
  "possible_cause": "Validation did not match expected result",
  "suggestion": "Review expected vs actual outcome"
}

---

## 📊 Failure Reporting

On test failure, the framework automatically:

- captures screenshots  
- analyzes failure using AI logic  
- generates structured JSON reports  

Location:

    reports/failure_analysis/

---

## 📊 Execution Dashboard

Provides a visual summary of test results:

- Total tests  
- Passed / Failed  
- Success rate  
- Failure types  

Generated after execution for quick analysis.

---

## 🧠 AI-Inspired Validation

Implements semantic validation strategies to reduce brittle assertions.

Instead of relying only on exact strings, the framework validates outcomes using intelligent logic.

---

## 🏗️ Architecture

### Page Object Model (POM)

Modular structure with clear separation of concerns.

### Domain Separation

- banking  
- qa_agent  
- smoke  

### Layers

- pages/ → UI abstraction  
- tests/ → Test scenarios  
- api/ → API integration layer  
- services/ → Business logic abstraction  
- utils/ → Helpers and infrastructure  
- ai/ → Failure analysis engine  
- config/ → Environment configuration  
- data/ → Test data  

---

## 📁 Project Structure

    pages/
    tests/
    api/
    services/
    utils/
    ai/
    config/
    data/
    mock_api/
    .github/workflows/

---

## 🐳 Mock API (Docker)

A fully functional mock banking API is included to simulate backend behavior.

Run with Docker:

    docker compose up --build

Base URL:

    http://127.0.0.1:5000

Available Endpoints:

- POST /login  
- GET /balance/<username>  
- POST /transfer  
- GET /history/<username>  
- POST /reset  

---

## ⚙️ CI/CD (GitHub Actions)

Automated test execution on:

- push  
- pull request  

Includes:

- QA Agent tests  
- Failure analysis artifact upload  
- Screenshot artifact upload  

---

## ▶️ Running Tests

Run all tests:

    pytest -v -s

Run non-mobile tests:

    pytest tests/qa_agent -v -s

Run by tag:

    pytest -m smoke -v
    pytest -m hybrid -v
    pytest -m api -v

---

## 💡 Why This Project

This project was designed to simulate real-world QA engineering challenges:

- scalable automation architecture  
- hybrid testing strategy  
- intelligent failure analysis  
- reproducible environments (Docker)  
- CI/CD integration  
- robust API interaction  
- structured test execution  

---

## 👨‍💻 Author

Mario Lima  
QA Automation Engineer focused on modern test architecture, AI-driven testing, and scalable QA solutions