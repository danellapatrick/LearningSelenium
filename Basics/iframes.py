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
driver.get("https://demoqa.com/frames")
driver.maximize_window()
driver.implicitly_wait(0.5)
driver.switch_to.frame("frame2")
heading=driver.find_element(By.ID,"sampleHeading")
heading=heading.text
if heading == "This is a sample page":
    print(heading)
    print("Passed")
else:
    print("Failed")


