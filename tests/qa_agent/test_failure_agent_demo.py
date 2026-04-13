from utils.qa_failure_agent import QAFailureAgent
import pytest

@pytest.mark.api



def test_failure_agent_demo():
    agent = QAFailureAgent()

    error_message = """
    selenium.common.exceptions.StaleElementReferenceException:
    Message: stale element reference: element is not attached to the page document
    """

    report = agent.format_report(error_message)

    assert "ui_synchronization" in report