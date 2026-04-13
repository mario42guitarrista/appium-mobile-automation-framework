import json
import os


def generate_html_dashboard(
    summary_file: str = "reports/execution_logs/execution_summary.json",
    output_file: str = "reports/execution_logs/dashboard.html"
) -> str:
    if not os.path.exists(summary_file):
        raise FileNotFoundError(f"Summary file not found: {summary_file}")

    with open(summary_file, "r", encoding="utf-8") as f:
        summary = json.load(f)

    failure_types = summary.get("failure_types", {})
    failure_items = ""
    if failure_types:
        for error_type, count in failure_types.items():
            failure_items += f"<li><strong>{error_type}</strong>: {count}</li>"
    else:
        failure_items = "<li>none</li>"

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>QA Execution Dashboard</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background: #f4f6f8;
                color: #222;
            }}
            .container {{
                max-width: 900px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            }}
            h1 {{
                margin-bottom: 20px;
            }}
            .grid {{
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 16px;
                margin-bottom: 24px;
            }}
            .card {{
                background: #f9fafb;
                border: 1px solid #e5e7eb;
                border-radius: 10px;
                padding: 20px;
            }}
            .label {{
                font-size: 14px;
                color: #555;
            }}
            .value {{
                font-size: 28px;
                font-weight: bold;
                margin-top: 8px;
            }}
            ul {{
                padding-left: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>QA Execution Dashboard</h1>

            <div class="grid">
                <div class="card">
                    <div class="label">Total tests</div>
                    <div class="value">{summary['total_tests']}</div>
                </div>
                <div class="card">
                    <div class="label">Passed</div>
                    <div class="value">{summary['passed']}</div>
                </div>
                <div class="card">
                    <div class="label">Failed</div>
                    <div class="value">{summary['failed']}</div>
                </div>
                <div class="card">
                    <div class="label">Success rate</div>
                    <div class="value">{summary['success_rate']}%</div>
                </div>
            </div>

            <div class="card">
                <h2>Failure types</h2>
                <ul>
                    {failure_items}
                </ul>
            </div>
        </div>
    </body>
    </html>
    """

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    return output_file