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
import re
from selenium.webdriver.support.ui import Select


def Cart(Veg1):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#")
    driver.maximize_window()
    driver.find_element(By.XPATH,
                        "//body/div[@id='root']/div[@class='container']/div[@class='products-wrapper']/div[@class='products']/div[1]/div[3]/button[1]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[@class='cart-icon']//img[contains(@class,'')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[contains(text(),'Place Order')]").click()
    time.sleep(2)
    select = Select(driver.find_element(By.XPATH,"//select[@style='width: 200px;']"))
    select.select_by_index(4)
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
    driver.find_element(By.XPATH,"//button[contains(text(),'Proceed')]").click()
    time.sleep(2)
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#")
element = driver.find_element(By.XPATH, "//div[@class='products']")
text = element.text
Vegetables = re.findall("[A-Z][a-z].+", text)
Vegetables1 = []
for fruits in Vegetables:
    findall = re.sub(".-.+", '', fruits)
    Vegetables1.append(findall)
print(Vegetables1)
driver.close()
Veg = input("Which Vegetable do you like to have?")
for v in Vegetables1:
    if v.__contains__(Veg):
        Veg2 = Vegetables1.index(v)
        Cart(Veg2 + 1)
else:
    print("No result")





