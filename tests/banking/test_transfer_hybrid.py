from api.account_api import AccountAPI
import pytest

@pytest.mark.hybrid
@pytest.mark.api

def test_transfer_api_validation():
    username = "mario_user"

    initial_balance_response = AccountAPI.get_balance(username)
    assert initial_balance_response["status_code"] == 200

    initial_balance = initial_balance_response["body"]["balance"]

    transfer_response = AccountAPI.transfer(username, 200)
    assert transfer_response["status_code"] == 200
    assert transfer_response["body"]["status"] == "success"

    updated_balance_response = AccountAPI.get_balance(username)
    assert updated_balance_response["status_code"] == 200

    updated_balance = updated_balance_response["body"]["balance"]

    assert updated_balance == initial_balance - 200