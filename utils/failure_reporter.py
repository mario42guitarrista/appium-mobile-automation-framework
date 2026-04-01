import os
import json
from datetime import datetime


def save_failure_analysis(test_name: str, analysis: dict, error_message: str) -> str:
    os.makedirs("reports/failure_analysis", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_test_name = test_name.replace("/", "_").replace("\\", "_").replace("::", "_")
    file_name = f"{safe_test_name}_{timestamp}.json"
    file_path = os.path.join("reports", "failure_analysis", file_name)

    payload = {
        "test_name": test_name,
        "timestamp": timestamp,
        "analysis": analysis,
        "error_message": error_message[:2000]
    }

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=4, ensure_ascii=False)

    return file_path