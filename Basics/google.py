import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver


def Register_Account():
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://blue.genetechz.com/pt-env/testing/?page_id=74")
    driver.maximize_window()

    driver.find_element(By.ID, "pie-33-field_gzWUFHEydI-34").send_keys("Check@mailinator.com")
    time.sleep(3)
    driver.find_element(By.ID, "pie-33-field_bPqOU2G2zG-34").send_keys("Check")
    time.sleep(3)
    driver.find_element(By.ID, "pie-33-field_lRrMt4doZW-34").send_keys('C://python-selenium/PythonSelenium/LearningSelenium/Uploads/dummy.pdf')
    time.sleep(3)
    driver.find_element(By.NAME, "pie_forms[submit]").click()
    time.sleep(5)

Register_Account()



