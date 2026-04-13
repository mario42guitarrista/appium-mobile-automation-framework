from services.transfer_service import TransferService
from api.account_api import AccountAPI
import pytest

@pytest.mark.smoke
@pytest.mark.hybrid
@pytest.mark.mobile


def test_transfer_ui_and_api_validation(driver):
    username = "mario_user"

    # 🔥 RESET 
    reset_response = AccountAPI.reset_data()
    assert reset_response["status_code"] == 200

    # 1. saldo inicial via API
    initial_balance_response = AccountAPI.get_balance(username)
    assert initial_balance_response["status_code"] == 200

    initial_balance = initial_balance_response["body"]["balance"]

    # 2. ação via UI + API (via service)
    service = TransferService(driver)
    result = service.transfer_and_sync_api(username, initial_balance, 200)

    assert result["ui_result"]["status"] == "success"
    assert result["api_result"]["status_code"] == 200
    assert result["api_result"]["body"]["status"] == "success"

    # 3. valida saldo final via API
    updated_balance_response = AccountAPI.get_balance(username)
    assert updated_balance_response["status_code"] == 200

    updated_balance = updated_balance_response["body"]["balance"]

    assert updated_balance == initial_balance - 200