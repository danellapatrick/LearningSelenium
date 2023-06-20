import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://demo.guru99.com/test/newtours/")
#wair some time here
driver.implicitly_wait(10)

assert  "Welcome: Mercury Tours" in driver.title
user_ele= driver.find_element(By.NAME, "userName")
print(user_ele.is_displayed()) # returns True or False based on element status
print(user_ele.is_enabled())

ele = driver.find_element(By.NAME, "password")
print(ele.is_displayed())  # returns True or False based on element status
print(ele.is_enabled())

user_ele.send_keys("mercury")
ele.send_keys("mercury")

driver.find_element(By.NAME, "submit").click()
driver.close()