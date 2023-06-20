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


def Register_Account(username,password):
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://blue3.genetechz.com/pieregister/registration-2/")
    driver.maximize_window()

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "email_1").send_keys('test11371@mailinator.com')
    driver.find_element(By.ID, "password_2").send_keys(password)
    time.sleep(3)
    driver.find_element(By.ID, "confirm_password_password_2").send_keys(password)
    time.sleep(3)
    #driver.presence_of_element_located(
     #   (By.XPATH, "//div[@id='upload_19']"))  # Example xpath
    #pyautogui.write('C://python-selenium/PythonSelenium/LearningSelenium/Uploads/dummy.pdf')
    #pyautogui.press('enter')
    driver.find_element(By.XPATH, "//div[@id='upload_19']").click()
    time.sleep(3)
    os.system("C:/Users/danella.patrick/Desktop/autoit/fileupload.exe")
    driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
    time.sleep(5)
#//input[@id='pie_register_fileList_upload_19']"
username = 'Test11371'
password = 'Danella@1290'
Register_Account(username, password)



