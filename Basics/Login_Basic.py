import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#username and Password
username_email = 'tehzeeb@yopmail.com'
password = 'admin'


# Set the path to your Chrome WebDriver executable
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


# Set delays (in seconds)
implicit_wait_time = 5
explicit_wait_time = 10

# Maximize the browser window
driver.maximize_window()

# Set the base URL
url = "https://nhmedsupply.com/my-account/"

# Navigate to the login page
driver.get(url) #/login
time.sleep(10)
# Wait for the username input field to be visible




# Wait for the page to load completely
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='username' or @id='email']")))

# Find the username or email input field using XPath and enter the username or email
username_email_input = driver.find_element(By.XPATH, "//input[@id='username' or @id='email']")
username_email_input.send_keys(username_email)
time.sleep(5)

# Add a delay to simulate human interaction
driver.implicitly_wait(2)
# Find the button to proceed after entering the username or email using XPath
proceed_button = None
try:
    proceed_button = driver.find_element(By.XPATH, "//button[@type='button' and not(contains(text(), 'Forgot Password')) and not(contains(text(), 'Sign Up'))]")
except:
    pass

# Click on the proceed button if it exists and does not contain "Forgot Password" text
if proceed_button:
    proceed_button.click()

# Wait for the page to load completely
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))

# Find the password input field using XPath and enter the password
password_input = driver.find_element(By.XPATH, "//input[@id='password']")
password_input.send_keys(password)

# Add a delay to simulate human interaction
driver.implicitly_wait(2)

# Find the submit button using XPath and click on it (input type or button type)
try:
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and not(contains(@value, 'Forgot Password'))]")
    submit_button.click()
except:
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and not(contains(text(), 'Forgot Password'))]")
    submit_button.click()



# Perform further actions after successful login

# Close the browser
driver.quit()



