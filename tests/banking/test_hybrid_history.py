from api.auth_api import AuthAPI
from api.account_api import AccountAPI
from pages.banking.menu_page import MenuPage


def test_hybrid_transaction_history(driver):
    auth_api = AuthAPI()
    account_api = AccountAPI()
    menu_page = MenuPage(driver)

    login_result = auth_api.login("admin", "1234")
    token = login_result["token"]

    api_history = account_api.get_transaction_history(token)
    ui_history = menu_page.get_transaction_history()

    assert api_history["status"] == "success"
    assert len(api_history["transactions"]) == len(ui_history)
    assert api_history["transactions"][0]["type"] == ui_history[0]["type"]