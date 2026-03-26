from pages.banking.login_page import LoginPage


def test_login_required_fields(driver):
    login = LoginPage(driver)

    result = login.validate_login("", "")

    assert result == "required_fields"


def test_login_invalid_credentials(driver):
    login = LoginPage(driver)

    result = login.validate_login("user", "wrong")

    assert result == "invalid_credentials"


def test_login_success(driver):
    login = LoginPage(driver)

    result = login.validate_login("admin", "1234")

    assert result == "success"