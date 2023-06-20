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


def Register_Account():
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://blue3.genetechz.com/pieregister/registration/")
    driver.maximize_window()

    driver.find_element(By.XPATH,"//input[@id='email_1']").send_keys("danella2@mailinator.com")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys('test1371')
    time.sleep(5)
    #driver.presence_of_element_located(
     #   (By.XPATH, "//div[@id='upload_19']"))  # Example xpath
    #pyautogui.write('C://python-selenium/PythonSelenium/LearningSelenium/Uploads/dummy.pdf')
    #pyautogui.press('enter')
    driver.find_element(By.XPATH, "//div[@id='upload_66']").click()
    time.sleep(3)
    os.system("C:/Users/danella.patrick/Desktop/autoit/fileupload.exe")
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='date_67_1']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@id='ui-datepicker-div']").is_displayed()
    time.sleep(4)
    driver.find_element(By.XPATH,"//a[@class='ui-state-default ui-state-highlight ui-state-hover']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='pie_wrap_buttons']//input[@type='submit']").click()
    time.sleep(5)

Register_Account()



