# Selenium code in Python to login using a username and password with Xpaths, adding delays, maximizing the screen, and submitting the form using a button element with a type attribute:
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



#username and Password
email = 'qadetyryko@mailinator.com'
password = 'Pa$$w0rd!'


# Set the path to your Chrome WebDriver executable
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.maximize_window()

# Set explicit wait time for the elements to be found
wait = WebDriverWait(driver, 10)

# Navigate to the login page
driver.get("http://bitereel.com/login")
# Wait for the page to load completely
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))

# Find the email input field using XPath and enter the email
email_input = driver.find_element(By.XPATH, "//input[@id='email']")
email_input.send_keys(email)

# Add a delay to simulate human interaction
driver.implicitly_wait(2)

# Find the password input field using XPath and enter the password
password_input = driver.find_element(By.XPATH, "//input[@type='password']")
password_input.send_keys(password)

# Add a delay to simulate human interaction
driver.implicitly_wait(2)

# Find the submit button using XPath and click on it
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()
time.sleep(4)

# Close the browser
driver.quit()
