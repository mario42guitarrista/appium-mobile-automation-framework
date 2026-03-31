import pytest
from pages.login_page import LoginPage

pytest.skip("Legacy smoke login. Banking flow is now the official implementation.", allow_module_level=True)

def test_login_success(driver):
    login = LoginPage(driver)
    login.login("user", "1234")

    assert driver.current_package == "com.android.chrome"


def test_login_invalid(driver):
    
    login = LoginPage(driver)
    login.login("user", "wrong")

    assert driver.current_package == "com.android.chrome"