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


def Padzee():
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://padzee.com/")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//a[@id='androidButton']").click()
    time.sleep(5)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(20)
    driver.get_screenshot_as_file("play.png")
    # time.sleep(5)
    print("The Second opened  window   = " + driver.title)
    driver.switch_to.window(driver.window_handles[0])
    print(driver.window_handles)
    driver.get_screenshot_as_file("play.png")
    time.sleep(5)
Padzee()




