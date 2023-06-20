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
from selenium.webdriver.common.action_chains import ActionChains

def Register_Account():
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://donatepakistan.laravel.genetechz.com/register")
    driver.maximize_window()

    driver.find_element(By.XPATH, "//body/div[@id='app']/div/main/section[@class='signUp-section flex flex-items-center flex-direction-col flex-justify-center']/div[@class='registration-form']/form[@class='el-form demo-ruleForm']/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("Danella")
    time.sleep(1)
    driver.find_element(By.XPATH, "//body/div[@id='app']/div/main/section[@class='signUp-section flex flex-items-center flex-direction-col flex-justify-center']/div[@class='registration-form']/form[@class='el-form demo-ruleForm']/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("Patrick")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@type='email']").send_keys("danella@mailinator.com")
    time.sleep(1)
    driver.find_element(By.XPATH,"//body/div[@id='app']/div/main/section[@class='signUp-section flex flex-items-center flex-direction-col flex-justify-center']/div[@class='registration-form']/form[@class='el-form demo-ruleForm']/div[2]/div[1]/div[1]/div[1]/input[1]").send_keys("Pa$$w0rd!")
    time.sleep(2)
    driver.find_element(By.XPATH,"//body/div[@id='app']/div/main/section[@class='signUp-section flex flex-items-center flex-direction-col flex-justify-center']/div[@class='registration-form']/form[@class='el-form demo-ruleForm']/div[2]/div[2]/div[1]/div[1]/input[1]").send_keys("Pa$$w0rd!")
    time.sleep(3)
    driver.find_element(By.XPATH, "//body/div[@id='app']/div/main/section[@class='signUp-section flex flex-items-center flex-direction-col flex-justify-center']/div[@class='registration-form']/form[@class='el-form demo-ruleForm']/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[contains(text(),'India')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//body/div[@id='app']/div/main/section[@class='signUp-section flex flex-items-center flex-direction-col flex-justify-center']/div[@class='registration-form']/form[@class='el-form demo-ruleForm']/div[@class='form-colfull']/div[2]/div[1]/div[1]/div[1]/input[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[contains(text(),'Andhra Pradesh')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//body/div[@id='app']/div/main/section[@class='signUp-section flex flex-items-center flex-direction-col flex-justify-center']/div[@class='registration-form']/form[@class='el-form demo-ruleForm']/div[4]/div[1]/div[1]/div[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[contains(text(),'Amadalavalasa')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='el-form-item form-coltwo']//div[@class='el-form-item__content']//div[@class='el-input']//input[@type='text']").send_keys(78864)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='el-checkbox__inner']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@type='button']").click()
    time.sleep(2)
Register_Account()



