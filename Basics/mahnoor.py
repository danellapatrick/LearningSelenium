from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://adahi-dev.icreed.io/')
time.sleep(5)
driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/form[1]/button[1]").click()
time.sleep(3)
# driver.find_element(By.XPATH,"//input[@id='username']").send_keys("fawad")
# time.sleep(3)
# driver.find_element(By.XPATH,"//input[@id='password']").send_keys("aimsol")
# time.sleep(3)
# driver.find_element(By.XPATH,"//button[contains(text(),'LOG IN')]").click()
# time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='socialButton-Google']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='identifierId']").send_keys("mahnoor.aimsol@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//div[@id='identifierNext']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/span[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]").send_keys("innovative123")
time.sleep(2)
driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/div[2]").click()
time.sleep(2)

driver.find_element(By.XPATH,"//a[@id='signup-label']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys("Mahnoor")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys("Anwar")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("mahnoorarora@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("Mahnoor")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Mahnoor29")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='password-confirm']").send_keys("Mahnoor29")
time.sleep(2)
driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[7]/input[1]").click()
time.sleep(7)


# driver.close()