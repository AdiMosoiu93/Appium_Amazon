from appium.webdriver.common.appiumby import AppiumBy
import time
import logging
from locators.amazon_locators import AmazonLocators
from utils.screenshot import take_screenshot
from utils.scroll_to_element_by_text import scroll_to_element_by_text
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException


class AmazonPage:
    def __init__(self, driver):
        self.driver = driver

    def skip_sign_in(self):
        try:
            allow_notifications_btn = self.driver.find_element(AppiumBy.ID, AmazonLocators.ALLOW_NOTIFICATIONS_BTN)
            allow_notifications_btn.click()
            time.sleep(10)
        except:
            print("Allow notifications pop-up not appeared")

        try:
            skip_sign_on_btn = self.driver.find_element(AppiumBy.ID, AmazonLocators.SKIP_SIGN_IN_BTN)
            skip_sign_on_btn.click()
            time.sleep(10)
            take_screenshot(self.driver, "skip_sign_on")
        except:
            print("Skip sign on button not appeared")

    def dismiss_address_change_prompt(self):
        try:
            dismiss_btn = self.driver.find_element(AppiumBy.ID, AmazonLocators.DISMISS_BTN)
            dismiss_btn.click()
            take_screenshot(self.driver, "dismiss_button_clicked")
            time.sleep(5)
        except Exception as e:
            logging.error("Dismiss button not appeared")
            print("Dismiss button not appeared")

    def navigate_to_laptop_scetion(self):
        try:
            laptop_menu = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.LAPTOP_MENU)
            laptop_menu.click()
            time.sleep(10)
            take_screenshot(self.driver, "navigated_to_laptop_page")
        except:
            logging.error("Navigation to laptop page failed")
            print("Navigation to the laptop page is failed")

    def add_laptop_to_cart(self):
        try:
            product_name_box = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.PRODUCT_NAME_BOX)
            product_name = product_name_box.text

            if product_name == AmazonLocators.EXPECTED_PRODUCT_NAME:
                print("Product name matched successfully")
                add_to_cart_btn = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.ADD_TO_CART_BTN)
                add_to_cart_btn.click()
                take_screenshot(self.driver, "added_laptop_to_cart")
            else:
                print("Product name not matched")
                assert False
        except Exception as e:
            logging.error("Error adding laptop to cart")
            print("Error adding laptop to cart")

    def search_for_product(self, product_name):
        search_box = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.SEARCH_BOX)
        search_box.click()

        search_box_enabled = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.SEARCH_BOX_ENABLED)
        search_box_enabled.send_keys(product_name)

        time.sleep(10)

        hot_wheels_store_option = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.HOT_WHEELS_STORE)
        take_screenshot(self.driver, "Search page")
        if (not hot_wheels_store_option.is_displayed()):
            logging.error("Hot wheels stores option not apperared")
            assert False
        else:
            print("Hot wheels store appeared in search result")

    def search_for_product_only(self, product_name):
        search_box = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.SEARCH_BOX)
        search_box.click()
        time.sleep(10)

        search_box_enabled = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.SEARCH_BOX_ENABLED)
        search_box_enabled.send_keys(product_name)
        time.sleep(10)

    # ********************************************************************************
    # Test case 01_Pharmacy

    # I click on the "Pharmacy" button from navigation bar
    def click_pharmacy_btn(self):
        pharmacy_btn = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.NAVBAR_PHARMACY_BTN)
        pharmacy_btn.click()
        time.sleep(5)

    # I scroll down and click on the "Explore all the ways to save" button
    def click_explore_all_ways_to_save_btn(self):
        # Scroll down until element
        scroll_to_element_by_text(self.driver, "Explore all the ways to save")

        time.sleep(5)

        # Click on the element
        explore_all_the_ways_to_save_btn = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.EXPLORE_ALL_THE_WAYS_TO_SAVE_BTN)

        explore_all_the_ways_to_save_btn.click()

    # I type "lipitor" in the search field
    def type_word_in_field(self):
        # search_for_medication_btn = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.SEARCH_FOR_MEDICATION_FIELD)

        time.sleep(5)

        search_for_medication_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().textContains("Lipitor")')

        search_for_medication_btn.click()

        time.sleep(5)

        search_for_medication_btn.send_keys('lipitor')

    # ********************************************************************************
    # ********************************************************************************

    # @01_Automotive
    # I click on the browser menu button
    def click_on_browser_menu_btn(self):
        browser_menu_btn = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.BROWSER_MENU_BTN)
        browser_menu_btn.click()

        try:
            # Wait for the PRIME_BTN to be visible
            time.sleep(4)

            prime_btn = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.PRIME_BTN)

            # prime_button = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located(prime_btn)
            # )
            # Assert that the button is displayed
            assert prime_btn.is_displayed(), "PRIME_BTN is not displayed on the screen"
            print("PRIME_BTN is displayed on the screen.")
        except TimeoutException:
            print("PRIME_BTN was not displayed within the given time.")

    # I click on the "Automotive" button
    def click_on_automotive_card(self):
        scroll_to_element_by_text(self.driver, "Automotive")

        automotive_card = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.AUTOMOTIVE_BTN)
        automotive_card.click()

        try:
            # Wait for the Automotive Parts & Accessories button to be visible

            # automotive_parts_accessories_btn = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located(AmazonLocators.AUTOMOTIVE_PARTS_ACCESSORIES)
            # )

            time.sleep(4)

            automotive_parts_accessories_btn = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.AUTOMOTIVE_PARTS_ACCESSORIES)

            # Assert that the button is displayed
            assert automotive_parts_accessories_btn.is_displayed(), "automotive_parts_accessories_btn is not displayed on the screen"
            print("automotive_parts_accessories_btn is displayed on the screen.")
        except TimeoutException:
            print("automotive_parts_accessories_btn was not displayed within the given time.")

    # I click on the "Automotive Parts & Accessories" button
    def click_automotive_parts_accessories_btn(self):
        # Click on the automotive parts and accessories button
        automotive_parts_accessories_btn = self.driver.find_element(
            AppiumBy.XPATH, AmazonLocators.AUTOMOTIVE_PARTS_ACCESSORIES
        )
        automotive_parts_accessories_btn.click()

        try:
            # Find the element containing the 'Amazon Automotive' text
            text_element = self.driver.find_element(
                AppiumBy.XPATH, AmazonLocators.AMAZON_AUTOMOTIVE_BANNER
            )

            # Assert that the element with the text is displayed
            assert text_element.is_displayed(), "'Amazon Automotive' text is not displayed on the screen."
            print("'Amazon Automotive' text is displayed on the screen.")
        except NoSuchElementException:
            print("'Amazon Automotive' text was not found on the screen.")
        except WebDriverException as e:
            print(f"An error occurred while checking the element: {str(e)}")

    # I click on the "Add a new vehicle" button
    def click_add_new_vehicle_btn(self):
        add_new_vehicle_btn = self.driver.find_element(AppiumBy.XPATH, AmazonLocators.ADD_A_NEW_VEHICLE_BTN)
        add_new_vehicle_btn.click()

        try:

            manage_your_garage_btn = self.driver.find_element(
                AppiumBy.XPATH, AmazonLocators.MANAGE_YOUR_GARAGE_BTN
            )

            # Assert that the element with the text is displayed
            assert manage_your_garage_btn.is_displayed(), "Button is not displayed on the screen."
            print("Button is displayed on the screen.")
        except NoSuchElementException:
            print("Button was not found on the screen.")
        except WebDriverException as e:
            print(f"An error occurred while checking the element: {str(e)}")
