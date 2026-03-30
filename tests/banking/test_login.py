import json
from pathlib import Path
from utils.logger import logger

from pages.banking.login_page import LoginPage


def load_users():
    file_path = Path("data/users.json")
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def test_login_data_driven(driver):
    logger.info("Starting login data-driven test")

    login = LoginPage(driver)
    users = load_users()

    for user in users:
        logger.info(f"Testing user: {user['username']}")

        result = login.validate_login(user["username"], user["password"])

        logger.info(f"Result: {result}")

        assert result == user["expected"]