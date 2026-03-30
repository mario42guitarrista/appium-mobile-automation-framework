from utils.qa_failure_agent import QAFailureAgent


def test_analyze_stale_element():
    agent = QAFailureAgent()

    result = agent.analyze_failure(
        "selenium.common.exceptions.StaleElementReferenceException"
    )

    assert result["category"] == "ui_synchronization"


def test_analyze_no_such_element():
    agent = QAFailureAgent()

    result = agent.analyze_failure(
        "selenium.common.exceptions.NoSuchElementException"
    )

    assert result["category"] == "locator_or_timing"


def test_analyze_timeout():
    agent = QAFailureAgent()

    result = agent.analyze_failure(
        "selenium.common.exceptions.TimeoutException"
    )

    assert result["category"] == "timeout"


def test_analyze_assertion_error():
    agent = QAFailureAgent()

    result = agent.analyze_failure(
        "AssertionError: expected success but got invalid_credentials"
    )

    assert result["category"] == "assertion_failure"