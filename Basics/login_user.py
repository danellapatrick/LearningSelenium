import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
from selenium.webdriver.support.ui import Select
import pandas as pd


def login_Account(email,password):
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://blue.genetechz.com/pt-env/qa/fresh/login/")
    driver.maximize_window()

    driver.find_element(By.NAME, "log").send_keys(email)
    time.sleep(1)
    driver.find_element(By.NAME, "pwd").send_keys(password)
    time.sleep(1)
    driver.find_element(By.NAME, "wp-submit").click()
    time.sleep(1)

df=pd.read_csv("Login Users.csv")
for index, row in df.iterrows():
    username=row['Email ']
    password=row['Password ']
    login_Account(username,password)



