from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@given('User launch chrome browser')
def lauch_browser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('Open Swag labs the web page')
def landing_page(context):
    context.driver.get("https://www.saucedemo.com/")


@When('Enter username "{user}" and password "{passw}"')
def enter_credentials(context,user,passw):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='username']").send_keys(user)
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='password']").send_keys(passw)

@When('Click on login button')
def click_LoginButton(context):
    context.driver.find_element(By.CSS_SELECTOR,"[value='Login']").click()


@then('Validate the product page')
def step_impl(context):
    productName = context.driver.find_element(By.XPATH, "//div[@class='header_label']//div[@class='app_logo']").text
    assert productName == "Swag Labs"
    context.driver.close()