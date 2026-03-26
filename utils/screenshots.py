import os
from datetime import datetime


def save_screenshot(driver, folder="screenshots"):
    os.makedirs(folder, exist_ok=True)
    file_name = datetime.now().strftime("%Y%m%d_%H%M%S.png")
    file_path = os.path.join(folder, file_name)
    driver.save_screenshot(file_path)
    return file_path
