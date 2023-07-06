# Selenium code in Python to login using a username and password with Xpaths, adding delays, maximizing the screen, and submitting the form using a button element with a type attribute:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



#username and Password
username = 'danella.patrick'
password = 'hello-12345'


# Set the path to your Chrome WebDriver executable
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.maximize_window()

# Set explicit wait time for the elements to be found
wait = WebDriverWait(driver, 10)

# Navigate to the login page
driver.get("http://intranet.genetech.pk/intranet/login")

# Find the username input field using XPath and enter the username
username_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='username']")))
username_input.send_keys(username)

# Add a delay to simulate human interaction
driver.implicitly_wait(2)

# Find the password input field using XPath and enter the password
password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']")))
password_input.send_keys(password)

# Add a delay to simulate human interaction
driver.implicitly_wait(2)

# Find the submit button using XPath and click on it
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
submit_button.click()


# Close the browser
driver.quit()

# Close the browser
driver.quit()
