from pages.banking.menu_page import MenuPage


def test_transaction_history_not_empty(driver):
    menu = MenuPage(driver)

    history = menu.get_transaction_history()

    assert len(history) > 0


def test_transaction_contains_transfer(driver):
    menu = MenuPage(driver)

    history = menu.get_transaction_history()

    assert any(item["type"] == "transfer" for item in history)