from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class MenuPage(BasePage):
    LOGOUT_BTN = (AppiumBy.ACCESSIBILITY_ID, "Logout")

    def logout(self):
        self.click(self.LOGOUT_BTN)
