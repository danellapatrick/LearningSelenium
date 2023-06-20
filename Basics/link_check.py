from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
from seleniumwire import webdriver
import pyautogui
import os
import re
from selenium.webdriver.common.action_chains import ActionChains



s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.co.in//")
driver.maximize_window()

list_links = driver.find_element(By.TAG_NAME,'a')

for link in list_links:
      try:
          a=link.get_attribute('href')
      except requests.exceptions.MissingSchema:
          print("Encountered MissingSchema Exception")
      except requests.exceptions.InvalidSchema:
          print("Encountered InvalidSchema Exception")
      except:
         print("Encountered Some other Exception")

driver.quit()