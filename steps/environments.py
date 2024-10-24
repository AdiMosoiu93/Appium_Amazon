from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome(executable_path='/Users/saikatbhattacharyya/Downloads/chromedriver-mac-x64 2/chromedriver')
    context.driver.maximize_window()

def after_all(context):
    context.driver.quit()