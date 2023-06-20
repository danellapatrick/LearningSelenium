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
driver.get("https://jakeandgino.com/podcasts/")

# Find all the podcast titles

title_elements = driver.find_element(By.TAG_NAME,"h3")

titles = [title_element.text for title_element in title_elements]

# Print the titles
for title in titles:
    print(title)


# Close the webdriver
driver.quit()
