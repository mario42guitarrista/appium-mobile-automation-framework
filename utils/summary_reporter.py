import json
import os


def print_execution_summary(summary_file: str = "reports/execution_logs/execution_summary.json") -> None:
    if not os.path.exists(summary_file):
        print("Execution summary file not found.")
        return

    with open(summary_file, "r", encoding="utf-8") as f:
        summary = json.load(f)

    print("\n=== Test Execution Summary ===")
    print(f"Total tests: {summary['total_tests']}")
    print(f"Passed: {summary['passed']}")
    print(f"Failed: {summary['failed']}")
    print(f"Success rate: {summary['success_rate']}%")

    failure_types = summary.get("failure_types", {})
    if failure_types:
        print("Failure types:")
        for error_type, count in failure_types.items():
            print(f" - {error_type}: {count}")
    else:
        print("Failure types: none")