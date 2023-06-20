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
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://spero.vkscentral.com/en/login")
driver.find_element(By.XPATH,"//input[@id='signin_username']").send_keys('pthibeault@vksapp.com')
driver.find_element(By.XPATH,"//input[@id='signin_password']").send_keys('eDf_io_w2gTJ')
time.sleep(4)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//header[contains(text(),'Filters')]").is_displayed()
time.sleep(4)

driver.find_element(By.XPATH,"//a[@data-atqa='btn_new_gbook']").click()
time.sleep(6)

driver.find_element(By.XPATH,"//textarea[contains(@class,'ml-text validate[required]')]").send_keys("Test")
#namee.click()
time.sleep(2)
driver.find_element(By.XPATH,"//label[contains(text(),'Author:')]").is_displayed()
time.sleep(2)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,"rw_7_input")))
driver.find_element(By.ID,"rw_7_input").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[@data-atqa='gJAzDq-VOXd09wm']").click()
#river.find_element(By.XPATH,"//span[@class='rw-dropdown-list-value'][contains(text(),'Binghamton, NY')]").is_displayed()
#driver.find_element(By.XPATH("//div[contains(@class,'m-frm-fld-pair folder-picker-ctnr')]//div[contains(@class,'folder-tree-box-wrapper')]")).is_displayed()
#a= ActionChains(driver)
#a.click(driver.find_element(By.XPATH,"//div[contains(@class,'m-frm-fld-pair folder-picker-ctnr')]//div[contains(@class,'folder-tree-box-wrapper')]//div[contains(@class,'has-custom-btn')]//button[contains(@type,'button')]")).perform()
time.sleep(5)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'m-frm-fld-pair folder-picker-ctnr')]//div[contains(@class,'folder-tree-box-wrapper')]//div[contains(@class,'has-custom-btn')]//button[@type='button']"))).click()
driver.find_element(By.XPATH,"//div[contains(@class,'rct-tree folder-tree')]").is_displayed()
time.sleep(6)
driver.find_element(By.XPATH,"//span[contains(text(),'VKS Samples')]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='project_erp_part_number']").send_keys(12345)
driver.find_element(By.XPATH,"//input[@id='project_external_id']").send_keys(45667)
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='project_product_revision']").send_keys(9549235)
time.sleep(4)
driver.find_element(By.XPATH,"//input[contains(@type,'submit')]").submit()
time.sleep(2)


