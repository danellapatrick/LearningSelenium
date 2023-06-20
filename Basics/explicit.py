import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://www.expedia.com/")
driver.maximize_window()

driver.find_element(By.CLASS_NAME,"uitk-tab-anchor uitk-tab-anchor-selected").click()



driver.close()