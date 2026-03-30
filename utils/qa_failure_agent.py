class QAFailureAgent:
    def analyze_failure(self, error_message: str) -> dict:
        text = error_message.lower()

        if "staleelementreferenceexception" in text or "stale element" in text:
            return {
                "category": "ui_synchronization",
                "probable_cause": "The element reference became invalid after the UI changed.",
                "suggestion": "Re-locate the element after interaction and use explicit waits."
            }

        if "nosuchelementexception" in text or "no such element" in text:
            return {
                "category": "locator_or_timing",
                "probable_cause": "The element was not found due to locator mismatch or insufficient wait time.",
                "suggestion": "Review the locator and add explicit waits before interaction."
            }

        if "timeoutexception" in text or "timeout" in text:
            return {
                "category": "timeout",
                "probable_cause": "The expected condition was not met within the configured timeout.",
                "suggestion": "Review application response time and increase or improve wait strategy."
            }

        if "assertionerror" in text or "assert " in text:
            return {
                "category": "assertion_failure",
                "probable_cause": "The actual result does not match the expected result.",
                "suggestion": "Review test data, business rule, and expected assertion."
            }

        return {
            "category": "unknown",
            "probable_cause": "The failure pattern is not mapped yet.",
            "suggestion": "Inspect stacktrace and extend the failure agent with a new rule."
        }