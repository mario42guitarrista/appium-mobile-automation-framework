class FailureAnalyzer:
    def analyze(self, error_message: str) -> dict:
        msg = error_message.lower()

        if "stale element" in msg:
            return self._build_response(
                "StaleElementReference",
                "Element reference became stale",
                "Re-locate element before interaction"
            )

        if "nosuchelementexception" in msg or "no such element" in msg:
            return self._build_response(
                "ElementNotFound",
                "Locator may be incorrect or element not loaded",
                "Review locator strategy and add explicit wait"
            )

        if "timeout" in msg:
            return self._build_response(
                "Timeout",
                "Operation exceeded expected time",
                "Investigate performance and synchronization"
            )

        if "assertionerror" in msg:
            return self._build_response(
                "AssertionFailure",
                "Validation did not match expected result",
                "Review expected vs actual outcome"
            )
        
        if "nameerror" in msg:
            return self._build_response(
                "NameError",
                "A referenced name or class was not defined",
                "Check missing imports, variable names, or refactoring leftovers"
            )

        if "attributeerror" in msg:
            return self._build_response(
                "AttributeError",
                "Object does not expose the expected method or attribute",
                "Verify class implementation and method names"
            )

        if "importerror" in msg:
            return self._build_response(
                "ImportError",
                "Module or symbol could not be imported correctly",
                "Review imports, file names, and circular dependencies"
            )

        
        return self._build_response(
            "Unknown",
            "Unmapped failure pattern",
            "Inspect logs and stacktrace"
        )

    def _build_response(self, error_type, cause, suggestion):
        return {
            "error_type": error_type,
            "possible_cause": cause,
            "suggestion": suggestion
        }