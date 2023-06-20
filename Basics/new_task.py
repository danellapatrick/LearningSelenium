import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
from selenium.webdriver.common.action_chains import ActionChains
import re

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://padzee.com/")
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window("secondtab")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#")
element = driver.find_element(By.XPATH, "//div[@class='products']")
text = element.text
Vegetables = re.findall("[A-Z][a-z].+", text)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
textarea = driver.find_element(By.XPATH,"//textarea[@id='code']")
textarea.click()
for fruits in Vegetables:
    findall = re.sub(".-.+", ' ', fruits)
    textarea.send_keys(findall)
    textarea.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='txtUrl']").send_keys("Vegetable_Cart")
time.sleep(1)
driver.find_element(By.XPATH,"//div[@class='save button']//input[@type='submit']").click()
time.sleep(2)
print(driver.current_url)
