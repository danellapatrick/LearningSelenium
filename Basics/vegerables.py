import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
import pyautogui
import os
import re
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#")
driver.maximize_window()
element=driver.find_element(By.XPATH,"//div[@class='products']")
time.sleep(5)
text=element.text
vegetables=re.findall("[A-Z][a-z]+.",text)
Vegetable=["vegetables"]
Vegetable.extend(vegetables)
print(Vegetable)