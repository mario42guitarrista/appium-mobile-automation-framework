from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import DEFAULT_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def type(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.click()
        element.clear()
        element.send_keys(text)
        return element

    def get_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text
