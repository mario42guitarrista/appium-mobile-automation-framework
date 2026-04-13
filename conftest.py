import os
import sys
import pytest

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from utils.screenshots import save_screenshot
from utils.failure_reporter import save_failure_analysis
from utils.execution_logger import log_test_event


@pytest.fixture
def driver():
    from utils.driver_factory import create_driver

    driver = create_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.passed:
        log_test_event(
            test_name=item.nodeid,
            status="passed"
        )

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        analysis = {}

        # Screenshot
        if driver:
            file_path = save_screenshot(driver)
            print(f"\nScreenshot salvo em: {file_path}")

        # AI Failure Analyzer
        try:
            from ai.failure_analyzer import FailureAnalyzer

            analyzer = FailureAnalyzer()
            error_message = str(report.longrepr)
            analysis = analyzer.analyze(error_message)

            print("\n=== AI Failure Analysis ===")
            for key, value in analysis.items():
                print(f"{key}: {value}")

            report_path = save_failure_analysis(
                test_name=item.nodeid,
                analysis=analysis,
                error_message=error_message
            )
            print(f"\nFailure analysis salva em: {report_path}")

        except Exception as e:
            print(f"\n[Analyzer Error] {e}")

        log_test_event(
            test_name=item.nodeid,
            status="failed",
            details=analysis
        )