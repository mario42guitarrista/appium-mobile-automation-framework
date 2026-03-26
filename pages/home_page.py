from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class HomePage(BasePage):
    BALANCE = (AppiumBy.ACCESSIBILITY_ID, "Saldo")

    def get_balance(self):
        return self.get_text(self.BALANCE)
