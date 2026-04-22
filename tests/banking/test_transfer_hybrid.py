import pytest
from api.account_api import AccountAPI
from utils.data_factory import generate_user, generate_password, generate_initial_balance


@pytest.mark.hybrid
@pytest.mark.api
def test_transfer_api_validation():
    username = generate_user()
    password = generate_password()
    initial_balance_value = generate_initial_balance()

    reset_response = AccountAPI.reset_data()
    assert reset_response["status_code"] == 200

    create_user_response = AccountAPI.create_user(
        username=username,
        password=password,
        balance=initial_balance_value
    )
    assert create_user_response["status_code"] == 201

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