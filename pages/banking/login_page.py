from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    PASSWORD = (AppiumBy.CLASS_NAME, "android.widget.EditText")

    def login(self, username, password):
        elements = self.driver.find_elements(*self.USERNAME)

        if len(elements) >= 2:
            elements[0].send_keys(username)
            elements[1].send_keys(password)

    def validate_login(self, username, password):
        # regra simulada (igual sistema real)
        if username == "" or password == "":
            return "required_fields"

        if username != "admin" or password != "1234":
            return "invalid_credentials"

        return "success"