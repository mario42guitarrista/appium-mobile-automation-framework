from services.transfer_service import TransferService
from pages.banking.home_page import HomePage
from utils.ai_validator import is_valid_transfer_message
import pytest

@pytest.mark.regression
@pytest.mark.mobile



def test_transfer_success(driver):
    service = TransferService(driver)

    result = service.transfer(1000.00, 200.00)

    message = "Transaction completed successfully"

    assert result["status"] == "success"
    assert is_valid_transfer_message(message)


def test_transfer_insufficient_balance(driver):
    home = HomePage(driver)
    service = TransferService(driver)

    current_balance = home.get_balance()
    result = service.transfer_with_insufficient_balance(current_balance, 1500.00)

    assert result["status"] == "insufficient_balance"
    assert result["new_balance"] == 1000.00


def test_transfer_invalid_amount(driver):
    home = HomePage(driver)
    service = TransferService(driver)

    current_balance = home.get_balance()
    result = service.transfer_invalid_amount(current_balance, 0)

    assert result["status"] == "invalid_amount"
    assert result["new_balance"] == 1000.00