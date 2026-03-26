import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ChromePage(BasePage):
    SEARCH_BOX = (AppiumBy.CLASS_NAME, "android.widget.EditText")

    def open_chrome(self):
        self.driver.activate_app("com.android.chrome")
        time.sleep(4)

    def search(self, text):
        self.open_chrome()

        # NÃO clicar - direto no send_keys
        search = self.wait.until(
            lambda d: d.find_element(*self.SEARCH_BOX)
        )

        search.send_keys(text)
        self.driver.press_keycode(66)

    def get_current_package(self):
        return self.driver.current_package