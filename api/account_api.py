import requests
from config.settings import BASE_API_URL


class AccountAPI:
    DEFAULT_TIMEOUT = 10

    @staticmethod
    def _safe_json(response) -> dict:
        try:
            return response.json()
        except Exception:
            return {
                "raw_response": response.text
            }

    @staticmethod
    def _build_response(response) -> dict:
        return {
            "status_code": response.status_code,
            "body": AccountAPI._safe_json(response)
        }

    @staticmethod
    def _handle_request(request_callable) -> dict:
        try:
            response = request_callable()
            return AccountAPI._build_response(response)
        except requests.exceptions.Timeout:
            return {
                "status_code": 0,
                "body": {
                    "error": "timeout",
                    "message": "The request timed out."
                }
            }
        except requests.exceptions.ConnectionError:
            return {
                "status_code": 0,
                "body": {
                    "error": "connection_error",
                    "message": "Could not connect to the API."
                }
            }
        except requests.exceptions.RequestException as e:
            return {
                "status_code": 0,
                "body": {
                    "error": "request_error",
                    "message": str(e)
                }
            }

    @staticmethod
    def get_balance(username: str) -> dict:
        return AccountAPI._handle_request(
            lambda: requests.get(
                f"{BASE_API_URL}/balance/{username}",
                timeout=AccountAPI.DEFAULT_TIMEOUT
            )
        )

    @staticmethod
    def get_history(username: str) -> dict:
        return AccountAPI._handle_request(
            lambda: requests.get(
                f"{BASE_API_URL}/history/{username}",
                timeout=AccountAPI.DEFAULT_TIMEOUT
            )
        )

    @staticmethod
    def transfer(username: str, amount: float) -> dict:
        return AccountAPI._handle_request(
            lambda: requests.post(
                f"{BASE_API_URL}/transfer",
                json={
                    "username": username,
                    "amount": amount
                },
                timeout=AccountAPI.DEFAULT_TIMEOUT
            )
        )

    @staticmethod
    def reset_data() -> dict:
        return AccountAPI._handle_request(
            lambda: requests.post(
                f"{BASE_API_URL}/reset",
                timeout=AccountAPI.DEFAULT_TIMEOUT
            )
        )