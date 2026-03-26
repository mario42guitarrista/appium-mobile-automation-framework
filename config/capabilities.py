from appium.options.android import UiAutomator2Options


def get_android_options():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.no_reset = True
    return options
