import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class LoginPage(BasePage):
    SEARCH_BOX = (AppiumBy.CLASS_NAME, "android.widget.EditText")

    def open_chrome(self):
        self.driver.activate_app("com.android.chrome")

    def login(self, user, password):
        # aqui estamos simulando o "login" usando a busca do Chrome
        self.open_chrome()
        self.click(self.SEARCH_BOX)
        time.sleep(1)
        self.type(self.SEARCH_BOX, "Appium Python")
        self.driver.press_keycode(66)

    def get_error(self):
        return "erro simulado"