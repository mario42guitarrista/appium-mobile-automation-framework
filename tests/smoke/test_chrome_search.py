from pages.chrome_page import ChromePage


def test_search_in_chrome(driver):
    chrome = ChromePage(driver)
    chrome.search("Appium Python")

    assert chrome.get_current_package() == "com.android.chrome"