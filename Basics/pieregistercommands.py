import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



#'''
# Condtional  Commands-
# is_displayed  is_enabled , is_selected #
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://blue3.genetechz.com/pieregister/login/")
user_ele= driver.find_element(By.NAME, "log")
ele = driver.find_element(By.NAME, "pwd")



def both_correct(username,password):
    user_ele.send_keys(username)
    ele.send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()
    account = driver.find_element(By.X, "piereg_profile_cont")
    time.sleep(5)
    account.is_displayed()
    print("login Success")
    driver.close()

try:

    username = 'Test17'
    password = 'Danella@1290'
    both_correct(username, password)
except Exception:
    print("Username or password is wrong")
