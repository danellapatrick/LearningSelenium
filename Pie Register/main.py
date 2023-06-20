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
driver.get("https://blue.genetechz.com/pt-env/qa/fresh/login/")
user_ele= driver.find_element(By.NAME, "log")
ele = driver.find_element(By.NAME, "pwd")
driver.maximize_window()



def both_correct(username,password):
    user_ele.send_keys(username)
    ele.send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()
    driver.find_element(By.XPATH, "//a[@class='ab-item'][contains(text(),'WordPress Test Site')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[contains(text(),'Pie Register')]").click()
    driver.find_element(By.XPATH,"//a[@class='wp-first-item current']").click()
# Clicking on Add new Button
    driver.find_element(By.XPATH,"//a[@class='button button-large button-primary']").click()

username = 'taha'
password = 'taha786'
both_correct(username, password)

