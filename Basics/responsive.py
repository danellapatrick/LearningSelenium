from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Set the screen sizes you want to test
screen_sizes = [(1024, 768), (1366, 768), (1920, 1080)]

# Configure Chrome options
s = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening browser window)


# Function to set the browser window size and take a screenshot
def set_window_size_and_capture_screenshot(width, height):
    driver.set_window_size(width, height)
    # Wait for the page to load (adjust the timeout as needed)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    screenshot = driver.execute_script("return document.documentElement.outerHTML")
    # Take a screenshot and save it
    with open(f"screenshot{width}x{height}.png", "wb") as file:
        file.write(screenshot.encode("utf-8"))


# Open the website

driver = webdriver.Chrome(service=s)
driver.get("https://kilbylaw.com/")
# Test the website in different screen sizes and capture screenshots
for size in screen_sizes:
    set_window_size_and_capture_screenshot(size[0], size[1])

# Quit the WebDriver
driver.quit()
