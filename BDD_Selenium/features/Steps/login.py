from behave import  *

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



@given('I launch Chrome browser')
def step_impl(context):
    s = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=s)


@when('I open Facebook Page')
def step_impl(context):
    context.driver.get("https://www.facebook.com/")
    context.driver.maximize_window()


@when(u'Enter the username and Password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("qateam786@gmail.com")
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("786qateam")
    time.sleep(3)



@when('Click Login')
def step_impl(context):
    context.driver.find_element(By.NAME, "login").click()
    time.sleep(10)

@then('It should successfully login')
def step_impl(context):
    context.driver.close()

