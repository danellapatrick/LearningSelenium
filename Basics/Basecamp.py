import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
from selenium.webdriver.common.action_chains import ActionChains


s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://3.basecamp.com/4957502/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("danella.patrick@genetechsolutions.com")
driver.find_element(By.XPATH,"//button[@type='button']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Danella@17")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(0.2)
a = ActionChains(driver)
t=driver.find_element(By.XPATH, "//h2[contains(text(),'QA Team')]")
a.context_click(t).key_down(Keys.CONTROL).click(t).perform()
driver.switch_to.window(driver.window_handles[1])
time.sleep(0.5)
element1 = driver.find_element(By.XPATH,"//span[contains(text(),'To-dos')]")

a.context_click(element1).key_down(Keys.CONTROL).click(element1).perform()
driver.switch_to.window(driver.window_handles[2])

driver.find_element(By.XPATH,"//span[@class='todolist__drag-handle']").click()

f=driver.find_element(By.XPATH,"//a[contains(text(),'Insert a to-do')]")
a.context_click(f).key_down(Keys.CONTROL).click(f).perform()
driver.switch_to.window(driver.window_handles[3])
time.sleep(3)
textarea = driver.find_element(By.XPATH,"//textarea[@id='todo_content']")
textarea.click()
textarea.send_keys("LMS Scenarios ")
textarea = driver.find_element(By.XPATH,"//textarea[@id='todo_content']")
textarea.click()
textarea.send_keys("LMS Scenarios ")

driver.implicitly_wait(0.5)
time.sleep(3)
assigned= driver.find_element(By.XPATH,"//input[@id='todo_assignees']")
assigned.send_keys("Danella Patrick")
assigned.send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)