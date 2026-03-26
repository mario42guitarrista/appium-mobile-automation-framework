import os
import sys
import pytest

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from utils.driver_factory import create_driver
from utils.screenshots import save_screenshot


@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            file_path = save_screenshot(driver)
            print(f"\nScreenshot salvo em: {file_path}")
