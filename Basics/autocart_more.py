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
import  re

def Cart(Cart1):
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#")
    driver.maximize_window()
    for i in Cart1:
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[@class='container']/div[@class='products-wrapper']/div[@class='products']/div[{}]/div[3]/button[1]".format(i)).click()
        time.sleep(5)
    driver.find_element(By.XPATH,"//a[@class='cart-icon']//img[contains(@class,'')]").click()
    time.sleep(10)
    driver.find_element(By.XPATH,"//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
    time.sleep(2)

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#")
element=driver.find_element(By.XPATH,"//div[@class='products']")
text=element.text

Vegetables=re.findall("[A-Z][a-z].+",text)
Vegetables1=["Veg"]
for fruits in Vegetables:
   findall=re.sub(".-.+",'',fruits)
   Vegetables1.append(findall)
print(Vegetables1)
driver.close()
Cart1=[]
Cart2=[]
Shop=int(input("How many Vegetables do you want to buy?"))
for i in range(Shop):
    Veg = input("Vegetable:")
    for v in Vegetables1:
        if v.__contains__(Veg):
            Veg2 = Vegetables1.index(v)
            Cart1.append(Veg2)
        else:
            Cart2.append(Vegetables1.index(v))

Cart(Cart1)











