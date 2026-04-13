import os
import json
from datetime import datetime


def log_test_event(test_name: str, status: str, details: dict | None = None) -> str:
    os.makedirs("reports/execution_logs", exist_ok=True)

    file_path = os.path.join("reports", "execution_logs", "test_execution.jsonl")

    payload = {
        "timestamp": datetime.now().isoformat(),
        "test_name": test_name,
        "status": status,
        "details": details or {}
    }

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")

    return file_path