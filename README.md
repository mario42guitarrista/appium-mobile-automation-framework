# Mobile Banking QA Automation Platform

Appium | Python | Pytest | CI/CD | Docker | Hybrid Testing | QA Observability

---

# 🚀 Overview

End-to-end QA automation platform simulating a real-world mobile banking system.

This project goes beyond traditional test automation by combining:

- Mobile automation
- API validation
- Hybrid testing
- AI-assisted failure analysis
- Parallel execution
- CI/CD integration
- Execution observability
- Dockerized backend environment

It was designed to reflect real QA engineering challenges found in modern distributed systems.

---

# 🧠 Key Highlights

- 📲 Mobile automation with Appium (Android Emulator)
- 🔄 End-to-end business flows
- 🔗 Hybrid testing strategy (API + UI validation)
- ⚡ Parallel test execution with pytest-xdist
- 📊 Dynamic test data generation
- 📈 Execution observability dashboard
- 🧾 HTML execution reports
- 🤖 AI-powered failure analysis
- ⚙️ CI/CD with GitHub Actions
- 🐳 Dockerized mock API environment

---

# 🏦 Business Scenarios Covered

## Authentication

- Required fields validation
- Invalid credentials
- Successful login
- Data-driven scenarios

## Balance

- Balance validation via API and UI

## Transfer

- Successful transfer
- Insufficient balance
- Invalid amount

## Transaction History

- History validation
- Transfer verification

## Full Flow

- Login → Balance → Transfer → Validation

---

# 🔗 Hybrid Testing (API + UI)

This project combines API and UI validation to reduce flaky tests and improve confidence in business validations.

Examples:

- Login validated via API and UI
- Balance validated via API and UI
- Transfer validated via API and business rules

---

# ⚡ Parallel Execution

The framework supports safe parallel execution using pytest-xdist.

Features:

- Isolated test execution
- Dynamic user generation
- Independent API validations
- Parallel workers support
- CI/CD-ready execution

Example:

```bash
pytest tests/qa_agent tests/banking/test_transfer_hybrid.py -n 2 -v -s
```

---

# 📊 Execution Observability Dashboard

The project includes an automated execution dashboard integrated into the CI/CD pipeline.

Features:

- Parallel execution metrics
- Execution duration tracking
- HTML execution reports
- GitHub Actions artifact generation
- CI environment visibility
- Automated dashboard generation

Dashboard example:

```text
Total Tests: 10
Passed: 10
Failed: 0
Parallel Workers: 2
Environment: GitHub Actions CI
```

Generated artifacts include:

- HTML execution reports
- Visual execution dashboard
- Execution logs
- Screenshots (when applicable)

Dashboard location:

```bash
reports/dashboard.html
```

---

# 🤖 AI Failure Analyzer

A custom-built failure analysis module integrated into the test execution lifecycle.

## Features

- Failure classification
- Root cause detection
- Suggested corrective actions
- Automatic execution on failure
- JSON report generation

## Example Output

```json
{
  "error_type": "AssertionFailure",
  "possible_cause": "Validation did not match expected result",
  "suggestion": "Review expected vs actual outcome"
}
```

---

# 📊 Failure Reporting

On test failure, the framework automatically:

- Captures screenshots
- Analyzes failures using AI logic
- Generates structured JSON reports

Location:

```bash
reports/failure_analysis/
```

---

# 🧠 AI-Inspired Validation

Implements semantic validation strategies to reduce brittle assertions.

Instead of relying only on exact strings, the framework validates outcomes using intelligent logic.

---

# 🏗️ Architecture

## Design Patterns

- Page Object Model (POM)
- Service Layer
- Modular Architecture
- Domain Separation

## Layers

```text
pages/      → UI abstraction
tests/      → Test scenarios
services/   → Business logic layer
api/        → API integration layer
utils/      → Helpers and infrastructure
qa_agent/   → Failure analysis engine
config/     → Environment configuration
data/       → Test data
```

---

# 📁 Project Structure

```text
pages/
tests/
services/
api/
utils/
config/
data/
mock_api/
reports/
.github/workflows/
```

---

# 🐳 Mock API (Docker)

A fully functional mock banking API is included to simulate backend behavior.

## Run with Docker

```bash
docker compose up --build
```

## Base URL

```text
http://127.0.0.1:5000
```

## Available Endpoints

```text
POST /login
POST /create_user
GET /balance/<username>
POST /transfer
GET /history/<username>
POST /reset
```

---

# ⚙️ CI/CD (GitHub Actions)

Automated pipeline execution on:

- Push
- Pull Request

Features:

- Parallel execution
- Dockerized environment
- HTML report generation
- Execution dashboard generation
- Artifact upload
- Non-mobile isolated execution

---

# 📦 CI/CD Artifacts

The pipeline automatically uploads:

- HTML execution reports
- Visual execution dashboard
- Logs
- Screenshots

Artifacts are available directly inside GitHub Actions.

---

# ▶️ Running Tests

## Run all tests

```bash
pytest -v -s
```

## Run non-mobile tests

```bash
pytest tests/qa_agent tests/banking/test_transfer_hybrid.py -n 2 -v -s
```

## Run tests with HTML report

```bash
pytest tests/qa_agent tests/banking/test_transfer_hybrid.py -n 2 -v -s --html=reports/html/report.html --self-contained-html
```

---

# 💡 Why This Project

This project was designed to simulate real-world QA engineering challenges:

- Scalable automation architecture
- Hybrid testing strategy
- Parallel execution
- CI/CD integration
- Intelligent failure analysis
- Execution observability
- Reproducible Docker environments

---

# 👨‍💻 Author

Mario Lima

QA Automation Engineer focused on:

- Modern test architecture
- Quality Engineering
- AI-driven testing
- CI/CD pipelines
- Scalable QA solutions
- Execution observability