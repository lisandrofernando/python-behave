from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('open the web page')
def openHomePage(context):
    context.driver.get("https://www.saucedemo.com/")


@then('verify the logo present in the page')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH,"//div[@class='login_logo'][text()='Swag Labs']").is_displayed()
    assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()