import pytest
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
import pandas as pd
from selenium.webdriver.support.ui import Select

@pytest.fixture()
def testopenBroswer(setup):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#")
    driver.maximize_window()
    return driver
    print("Broswer Launched")

def testAddtoCart():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#")
    driver.maximize_window()
    for i in range(1,5):
        driver.find_element(By.XPATH,
                        "//body/div[@id='root']/div[@class='container']/div[@class='products-wrapper']/div[@class='products']/div[{}]/div[3]/button[1]".format(i)).click()
        time.sleep(2)
    driver.find_element(By.XPATH, "//a[@class='cart-icon']//img[contains(@class,'')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]").click()

    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()
    time.sleep(2)
    select = Select(driver.find_element(By.XPATH, "//select[@style='width: 200px;']"))
    select.select_by_index(4)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Proceed')]").click()
    time.sleep(2)
    print("Item added Successfully")

def testRemovefromCart():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#")
    driver.maximize_window()

    driver.find_element(By.XPATH,
                            "//body/div[@id='root']/div[@class='container']/div[@class='products-wrapper']/div[@class='products']/div[1]/div[3]/button[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@class='cart-icon']//img[contains(@class,'')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/header[1]/div[1]/div[3]/div[2]/div[1]/div[1]/ul[1]/li[1]/a[1]").click()
    time.sleep(2)
    print("Cart is Empty")