from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
#driver = webdriver.Chrome(executable_path="C:\\Browers\\chromedriver.exe")
driver.get("https://lasik.2020lasikindianapolis.com/")
driver.maximize_window()
print(driver.title)
driver.close()