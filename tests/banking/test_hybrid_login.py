from api.auth_api import AuthAPI
from pages.banking.login_page import LoginPage


def test_hybrid_login_success(driver):
    api = AuthAPI()
    login_page = LoginPage(driver)

    api_result = api.login("admin", "1234")
    ui_result = login_page.validate_login("admin", "1234")

    assert api_result["status"] == "success"
    assert ui_result == "success"