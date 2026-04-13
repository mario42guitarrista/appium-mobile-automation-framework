import os
import json
from collections import Counter


def generate_execution_summary(
    input_file: str = "reports/execution_logs/test_execution.jsonl",
    output_file: str = "reports/execution_logs/execution_summary.json"
) -> dict:
    if not os.path.exists(input_file):
        return {
            "total_tests": 0,
            "passed": 0,
            "failed": 0,
            "success_rate": 0.0,
            "failure_types": {}
        }

    total_tests = 0
    passed = 0
    failed = 0
    failure_counter = Counter()

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue

            event = json.loads(line)
            total_tests += 1

            status = event.get("status")
            details = event.get("details", {})

            if status == "passed":
                passed += 1
            elif status == "failed":
                failed += 1
                error_type = details.get("error_type", "Unknown")
                failure_counter[error_type] += 1

    success_rate = round((passed / total_tests) * 100, 2) if total_tests else 0.0

    summary = {
        "total_tests": total_tests,
        "passed": passed,
        "failed": failed,
        "success_rate": success_rate,
        "failure_types": dict(failure_counter)
    }

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4, ensure_ascii=False)

    return summary