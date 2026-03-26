from pages.banking.home_page import HomePage


def test_balance_is_visible(driver):
    home = HomePage(driver)

    assert home.is_balance_visible() is True


def test_balance_value_is_correct(driver):
    home = HomePage(driver)

    assert home.get_balance() == 1000.00