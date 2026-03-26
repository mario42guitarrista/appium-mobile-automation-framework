from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class TransferPage(BasePage):
    VALUE = (AppiumBy.XPATH, "//android.widget.EditText")
    SEND_BTN = (AppiumBy.ACCESSIBILITY_ID, "Transferir")
    ERROR = (AppiumBy.XPATH, "//android.widget.TextView")

    def transfer(self, value):
        self.type(self.VALUE, value)
        self.click(self.SEND_BTN)

    def get_error(self):
        return self.get_text(self.ERROR)
