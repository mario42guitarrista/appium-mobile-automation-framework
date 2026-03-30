from pages.banking.login_page import LoginPage
from pages.banking.home_page import HomePage
from pages.banking.transfer_page import TransferPage
from utils.logger import logger


def test_full_flow_transfer(driver):
    logger.info("Starting full flow test")

    login = LoginPage(driver)
    home = HomePage(driver)
    transfer = TransferPage(driver)

    logger.info("Logging in")
    login.validate_login("admin", "1234")

    logger.info("Getting initial balance")
    initial_balance = home.get_balance()

    logger.info(f"Initial balance: {initial_balance}")

    logger.info("Performing transfer")
    result = transfer.transfer(initial_balance, 100)

    logger.info(f"Transfer result: {result}")

    assert result["status"] == "success"
    assert result["new_balance"] == initial_balance - 100