import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://lasik.2020lasikindianapolis.com/")
print(driver.title)
driver.get("https://www.stevedsims.com/")
time.sleep(5)
print(driver.title)
driver.back()
time.sleep(5)
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)
#'''
# Condtional  Commands-
# is_displayed  is_enabled , is_selected #
