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
import pyautogui
import os
import re
from selenium.webdriver.common.action_chains import ActionChains



s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://www.prowomen.pk/")
driver.maximize_window()
broken_links = 0
valid_links = 0

#get all links
all_links = driver.find_elements(By.TAG_NAME,"a")

for link in all_links:
    try:
        request = requests.head(link.get_attribute('href'), data={'key': 'value'})
        print("Status of " + link.get_attribute('href') + " is " + str(request.status_code))
        if (request.status_code >= 400):
            broken_links = (broken_links + 1)
        else:
            valid_links = (valid_links + 1)
    except requests.exceptions.MissingSchema:
        print("Encountered MissingSchema Exception")
        print(link.get_attribute('href'))
    except requests.exceptions.InvalidSchema:
        print("Encountered InvalidSchema Exception")
    except:
        print("Encountered Some other execption")

print("Detection of broken links completed with " + str(broken_links) + " broken links and " + str(
    valid_links) + " valid links")
