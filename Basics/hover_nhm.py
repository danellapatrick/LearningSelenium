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

def hover():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://nhmedsupplystg.wpengine.com/")
    driver.maximize_window()
    driver.implicitly_wait(0.5)
    a=ActionChains(driver)
    m=driver.find_element(By.XPATH,"//header/div[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]")
    a.move_to_element(m).perform()
    time.sleep(3)
    driver.find_element(By.XPATH,"//header/div[1]/div[1]/nav[1]/ul[1]/li[2]/ul[1]").is_enabled()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Shop by Category").click()
    time.sleep(3)
hover()