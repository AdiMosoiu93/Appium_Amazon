import os
from datetime import datetime

def take_screenshot(driver, screenshot_name):
    screenshot_dir = 'screenshots'
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot_file = os.path.join(screenshot_dir, f"{screenshot_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_file)
    print(f"Screenshot saved to {screenshot_file}")