from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class HistoryPage(BasePage):
    LAST_TRANSACTION = (AppiumBy.XPATH, "//android.widget.TextView[1]")

    def get_last_transaction(self):
        return self.get_text(self.LAST_TRANSACTION)
