import requests
from config.settings import BASE_API_URL


class AccountAPI:
    @staticmethod
    def get_balance(username: str) -> dict:
        response = requests.get(f"{BASE_API_URL}/balance/{username}")

        return {
            "status_code": response.status_code,
            "body": response.json()
        }

    @staticmethod
    def get_history(username: str) -> dict:
        response = requests.get(f"{BASE_API_URL}/history/{username}")

        return {
            "status_code": response.status_code,
            "body": response.json()
        }

    @staticmethod
    def transfer(username: str, amount: float) -> dict:
        response = requests.post(
            f"{BASE_API_URL}/transfer",
            json={
                "username": username,
                "amount": amount
            }
        )

        return {
            "status_code": response.status_code,
            "body": response.json()
        }