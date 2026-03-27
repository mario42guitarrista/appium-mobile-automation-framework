from api.auth_api import AuthAPI
from api.account_api import AccountAPI
from pages.banking.home_page import HomePage


def test_hybrid_balance_validation(driver):
    auth_api = AuthAPI()
    account_api = AccountAPI()
    home_page = HomePage(driver)

    login_result = auth_api.login("admin", "1234")
    token = login_result["token"]

    api_balance = account_api.get_balance(token)
    ui_balance = home_page.get_balance()

    assert api_balance["status"] == "success"
    assert api_balance["balance"] == ui_balance