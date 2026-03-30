from utils.logger import logger


class QAFailureAgent:
    def analyze_failure(self, error_message: str) -> dict:
        text = error_message.lower()

        logger.info("Analyzing failure message")

        if "staleelementreferenceexception" in text or "stale element" in text:
            result = {
                "category": "ui_synchronization",
                "probable_cause": "The element reference became invalid after the UI changed.",
                "suggestion": "Re-locate the element after interaction and use explicit waits."
            }
            logger.info(f"Failure categorized as: {result['category']}")
            return result

        if "nosuchelementexception" in text or "no such element" in text:
            result = {
                "category": "locator_or_timing",
                "probable_cause": "The element was not found due to locator mismatch or insufficient wait time.",
                "suggestion": "Review the locator and add explicit waits before interaction."
            }
            logger.info(f"Failure categorized as: {result['category']}")
            return result

        if "timeoutexception" in text or "timeout" in text:
            result = {
                "category": "timeout",
                "probable_cause": "The expected condition was not met within the configured timeout.",
                "suggestion": "Review application response time and improve the wait strategy."
            }
            logger.info(f"Failure categorized as: {result['category']}")
            return result

        if "assertionerror" in text or "assert " in text:
            result = {
                "category": "assertion_failure",
                "probable_cause": "The actual result does not match the expected result.",
                "suggestion": "Review business rules, test data, and expected assertions."
            }
            logger.info(f"Failure categorized as: {result['category']}")
            return result

        result = {
            "category": "unknown",
            "probable_cause": "The failure pattern is not mapped yet.",
            "suggestion": "Inspect the stacktrace and extend the failure agent with a new rule."
        }
        logger.info(f"Failure categorized as: {result['category']}")
        return result

    def format_report(self, error_message: str) -> str:
        analysis = self.analyze_failure(error_message)

        report = (
            f"Category: {analysis['category']}\n"
            f"Probable cause: {analysis['probable_cause']}\n"
            f"Suggestion: {analysis['suggestion']}"
        )

        logger.info("Failure report generated")
        return report