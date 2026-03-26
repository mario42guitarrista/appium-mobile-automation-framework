from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    PASSWORD = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    LOGIN_BTN = (AppiumBy.ACCESSIBILITY_ID, "Login")

    def login(self, username, password):
        elements = self.driver.find_elements(*self.USERNAME)

        if len(elements) >= 2:
            elements[0].send_keys(username)
            elements[1].send_keys(password)

        # botão ainda simulado
        # self.click(self.LOGIN_BTN)