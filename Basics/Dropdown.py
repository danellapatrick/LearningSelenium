import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
from selenium.webdriver.support.ui import Select
import pandas as pd


def Register_Account(email,password):
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://blue.genetechz.com/pt-env/testing/?page_id=6")
    driver.maximize_window()

    driver.find_element(By.XPATH, "//input[@id='pie-32-field_USwZuOoAbl-33']").send_keys(email)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='pie-32-field_gApUSE6Foa-33']").send_keys(password)
    time.sleep(3)
    select=Select(driver.find_element(By.XPATH, "//select[@id='pie-32-field_xp7n6jqDpe-33']"))
    select.select_by_index(10)
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='pie-32-field_0MzyxVUMeX-33']").click()
    driver.find_element(By.NAME, "pie_forms[submit]").click()
    time.sleep(5)


Register_Account('check',"check@mailinator.com")



