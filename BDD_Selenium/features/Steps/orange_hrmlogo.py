from behave import  *

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By




@given('launch chrome broswer')
def step_impl(context):
    s = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=s)


@when('open orange hrm homepage')
def step_impl(context):
    context.driver.get("https://padzee.com/")
    context.driver.maximize_window()


@then('verify that the logo present on the page')
def step_impl(context):
    status=context.driver.find_element(By.XPATH,"//img[@alt='Padzee']").is_displayed()
    assert status is True




@then('close browser')
def step_impl(context):
    context.driver.close()