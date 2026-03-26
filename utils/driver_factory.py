from appium import webdriver
from config.capabilities import get_android_options
from config.settings import APPIUM_SERVER_URL


def create_driver():
    options = get_android_options()
    return webdriver.Remote(APPIUM_SERVER_URL, options=options)
