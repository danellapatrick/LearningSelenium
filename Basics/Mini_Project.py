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

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://padzee.com/")
driver.maximize_window()
time.sleep(2)
textarea = driver.find_element(By.XPATH, "//textarea[@id='code']")
textarea.click()
df1 = pd.read_csv("test.csv")
a = []
b = []
c = []
for index, row in df1.iterrows():
    cola = str(row['col A'])
    colb = str(row['col B '])
    colc = str(row['col C  '])
    a.append(cola+' ')
    b.append(colb+' ')
    c.append(colc+' ')
textarea.send_keys(str(df1.columns),'\n',a,'\n',b,'\n',c)
textarea.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='txtUrl']").send_keys("Test_CSV")
time.sleep(1)
driver.find_element(By.XPATH,"//div[@class='save button']//input[@type='submit']").click()
time.sleep(2)

