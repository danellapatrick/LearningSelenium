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
from selenium.webdriver.common.alert import Alert

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://padzee.com/")
driver.maximize_window()
time.sleep(2)
def after_refresh():

    list1=[]
    list2=[]
    for i in range(3):
        i1 = input("Enter the elements of list 1")
        list1.append(i1)
    for j in range(3):
        j1=input("Enter the elements of list 2")
        list2.append(j1)

    df2 = pd.DataFrame(zip(list1,list2),columns=['fruits', 'rates'])
    df2.to_csv('C:/Users/danella.patrick/Desktop/basic.csv')
    path1 = 'C:/Users/danella.patrick/Desktop/basic.csv'
    driver.maximize_window()
    textarea = driver.find_element(By.XPATH, "//textarea[@id='code']")
    textarea.click()
    df1 = pd.read_csv(path1)
    a = []
    b = []
    for index, row in df1.iterrows():
        cola = str(row['fruits'])
        colb = str(row['rates'])
        a.append(cola + ' ')
        b.append(colb + ' ')
    textarea.send_keys(str(df1.columns), '\n', a, '\n', b, '\n')
    textarea.send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='txtUrl']").send_keys("Test_CSV")
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@class='save button']//input[@type='submit']").click()
    time.sleep(2)
    driver.close()

def read_data(path,column,columnb):
    textarea = driver.find_element(By.XPATH, "//textarea[@id='code']")
    textarea.click()
    df1 = pd.read_csv(path)
    a = []
    b = []
    for index, row in df1.iterrows():
        cola = str(row[column])
        colb = str(row[columnb])
        a.append(cola+' ')
        b.append(colb+' ')
    textarea.send_keys(str(df1.columns),'\n',a,'\n',b,'\n')
    textarea.send_keys(Keys.ENTER)
    time.sleep(3)
    driver.refresh()
    Alert(driver).accept()
    driver.minimize_window()

path2='test.csv'
column11='col A'
column21='col B '
read_data(path2,column11,column21)
after_refresh()