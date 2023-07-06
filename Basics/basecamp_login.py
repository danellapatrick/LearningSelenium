#Selenium code in Python to login using a email and password with Xpaths , adding delays, maximizing the screen, and submitting the form using a input element with a type attribute, waiting for the sit to load, clicking a button  after entering a email with attribute type  and element button to enter the password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Navigate to the login page
s=Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=s)
driver.maximize_window()
# Set implicit wait time for the elements to be found
driver.implicitly_wait(10)
driver.get("https://3.basecamp.com/4957502/")
#Username/email and pwd
username="danella.patrick@genetechsolutions.com"
password="Danella@17"


# Wait for the page to load completely
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']")))

# Find the email input field using XPath and enter the email
email_input = driver.find_element(By.XPATH, "//input[@id='username']")
email_input.send_keys(username)

# Add a delay to simulate human interaction
driver.implicitly_wait(2)

# Find the button to proceed with email entry and click on it
email_button = driver.find_element(By.XPATH, "//button[@type='button']")
email_button.click()

# Wait for the password input field to become visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))

# Find the password input field using XPath and enter the password
password_input = driver.find_element(By.XPATH, "//input[@type='password']")
password_input.send_keys([password])

# Add a delay to simulate human interaction
driver.implicitly_wait(2)

# Find the submit button using XPath and click on it
submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_button.click()



# Perform further actions after successful login

# Close the browser
driver.quit()
