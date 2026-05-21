from datetime import datetime


def generate_dashboard(
    total_tests,
    passed,
    failed,
    execution_time,
    workers,
    environment="CI/CD"
):
    html_content = f"""
    <html>
    <head>
        <title>QA Execution Dashboard</title>

        <style>
            body {{
                font-family: Arial;
                background-color: #0f172a;
                color: white;
                padding: 40px;
            }}

            h1 {{
                color: #38bdf8;
            }}

            .container {{
                display: flex;
                gap: 20px;
                flex-wrap: wrap;
            }}

            .card {{
                background: #1e293b;
                padding: 20px;
                border-radius: 12px;
                width: 220px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
            }}

            .title {{
                font-size: 18px;
                margin-bottom: 10px;
                color: #94a3b8;
            }}

            .value {{
                font-size: 32px;
                font-weight: bold;
            }}

            .success {{
                color: #22c55e;
            }}

            .failed {{
                color: #ef4444;
            }}

            .info {{
                color: #38bdf8;
            }}
        </style>
    </head>

    <body>

        <h1>QA Automation Dashboard</h1>

        <p>
            Last execution:
            {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        </p>

        <div class="container">

            <div class="card">
                <div class="title">Total Tests</div>
                <div class="value info">{total_tests}</div>
            </div>

            <div class="card">
                <div class="title">Passed</div>
                <div class="value success">{passed}</div>
            </div>

            <div class="card">
                <div class="title">Failed</div>
                <div class="value failed">{failed}</div>
            </div>

            <div class="card">
                <div class="title">Execution Time</div>
                <div class="value info">{execution_time}s</div>
            </div>

            <div class="card">
                <div class="title">Parallel Workers</div>
                <div class="value info">{workers}</div>
            </div>

            <div class="card">
                <div class="title">Environment</div>
                <div class="value info">{environment}</div>
            </div>

        </div>

    </body>
    </html>
    """

    output_path = "reports/dashboard.html"

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"Dashboard generated: {output_path}")