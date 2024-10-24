from appium.webdriver.common.appiumby import AppiumBy


def scroll_to_element_by_text(driver, text):

    return driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))'
    )
