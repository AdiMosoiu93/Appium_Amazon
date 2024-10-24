from behave import given, when, then
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time
from utils.screenshot import take_screenshot
import logging
import json
from pages.amazon_page import AmazonPage
import pandas as pd
import mysql.connector

logging.basicConfig(level=logging.INFO)

capabilities = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'Pixel 7 API 31',
    'app': "C:/Users/Dev/Desktop/APK Files/Amazon.apk",
    'appPackage': 'com.amazon.mShop.android.shopping',
    'appActivity': 'com.amazon.mShop.home.HomeActivity',
    'language': 'en',
    'locale': 'US'
}

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


@given('the Amazon app is launched')
def step_impl(context):
    context.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
    time.sleep(5)
    context.amazon_page = AmazonPage(context.driver)
    take_screenshot(context.driver, "app_launched")


@when('I skip sign-in')
def step_impl(context):
    context.amazon_page.skip_sign_in()
    time.sleep(10)


@when('I dismiss the address change prompt')
def step_impl(context):
    context.amazon_page.dismiss_address_change_prompt()


@when('I navigate to the laptop section')
def step_impl(context):
    context.amazon_page.navigate_to_laptop_scetion()


@then('I add the specified laptop to the cart')
def step_impl(context):
    context.amazon_page.add_laptop_to_cart()
    context.driver.quit()


@then('I search for "{product_name}" in search bar')
def step_impl(context, product_name):
    context.amazon_page.search_for_product(product_name)


@given('I have JSON data')
def step_impl(context):
    with open('data/data.json', 'r') as file:
        global json_data
        json_data = json.load(file)


@then('I am able access JSON data')
def step_impl(context):
    print(json_data['product_name'])
    json_data['param2']


@when('I read data from excel and search product')
def step_impl(context):
    context.df = pd.read_excel('data/data.xlsx')
    context.amazon_page.search_for_product_only(context.df['Product'])
    time.sleep(5)


@when('I read data from db and search product')
def step_impl(context):
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=8080,
        user='root',
        password='root',
        database='mydb'
    )

    df = pd.read_sql_query('SELECT product FROM product', conn)
    product_list = df['product'].tolist()
    context.df = product_list
    context.amazon_page.search_for_product_only(context.df)


# Test case 01_Pharmacy
@when('I click on the "Pharmacy" button from navigation bar')
def step_impl(context):
    context.amazon_page.click_pharmacy_btn()


@when('I scroll down and click on the "Explore all the ways to save" button')
def step_impl(context):
    context.amazon_page.click_explore_all_ways_to_save_btn()


@when('I type "lipitor" in the search field')
def step_impl(context):
    context.amazon_page.type_word_in_field()


# Test case 01_Automotive
@when('I click on the browser menu button')
def step_impl(context):
    context.amazon_page.click_on_browser_menu_btn()


@when('I click on the "Automotive" button')
def step_impl(context):
    context.amazon_page.click_on_automotive_card()


@when('I click on the "Automotive Parts & Accessories" button')
def step_impl(context):
    context.amazon_page.click_automotive_parts_accessories_btn()


@when('I click on the "Add a new vehicle" button')
def step_impl(context):
    context.amazon_page.click_add_new_vehicle_btn()
