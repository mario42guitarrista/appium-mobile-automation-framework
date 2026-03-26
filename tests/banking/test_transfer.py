from pages.banking.home_page import HomePage
from pages.banking.transfer_page import TransferPage


def test_transfer_success(driver):
    home = HomePage(driver)
    transfer = TransferPage(driver)

    current_balance = home.get_balance()
    result = transfer.transfer(current_balance, 200.00)

    assert result["status"] == "success"
    assert result["new_balance"] == 800.00


def test_transfer_insufficient_balance(driver):
    home = HomePage(driver)
    transfer = TransferPage(driver)

    current_balance = home.get_balance()
    result = transfer.transfer(current_balance, 1500.00)

    assert result["status"] == "insufficient_balance"
    assert result["new_balance"] == 1000.00


def test_transfer_invalid_amount(driver):
    home = HomePage(driver)
    transfer = TransferPage(driver)

    current_balance = home.get_balance()
    result = transfer.transfer(current_balance, 0)

    assert result["status"] == "invalid_amount"
    assert result["new_balance"] == 1000.00