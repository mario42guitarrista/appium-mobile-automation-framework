import requests
from config.settings import BASE_API_URL


class AuthAPI:
    @staticmethod
    def login(username: str, password: str) -> dict:
        response = requests.post(
            f"{BASE_API_URL}/login",
            json={
                "username": username,
                "password": password
            }
        )

        return {
            "status_code": response.status_code,
            "body": response.json()
        }