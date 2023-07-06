import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def mannual():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    driver.maximize_window()

    # Navigate to the website and locate the "Contact Us" link
    driver.get("https://nutriwest.staging.genetechz.com/")  # Replace with the actual URL of the website
    singup_link = driver.find_element(By.XPATH, "//a[contains(., 'Sign In As Provider')]")
    time.sleep(5)
    singup_link.click()
    #a=ActionChains(driver)
    #a.context_click(singup_link).key_down(Keys.CONTROL).click(singup_link).perform()
    #driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    email="gtechprovider@yopmail.com"
    driver.find_element(By.NAME,"email").send_keys(email)
    driver.find_element(By.NAME,"password").send_keys("admin123")
    driver.find_element(By.XPATH,"//body[1]/main[1]/section[2]/div[1]/div[1]/form[1]/div[3]/div[2]/input[2]").click()
    time.sleep(10)
    driver.find_element(By.XPATH,"//body[1]/main[1]/section[2]/div[1]/form[1]/div[1]/input[1]").click()
    driver.find_element(By.XPATH,"//body[1]/main[1]/section[2]/div[1]/form[1]/div[2]/input[1]").click()
    time.sleep(8)

    a = ActionChains(driver)
    m = driver.find_element(By.XPATH, "//a[contains(text(),'Products')]")
    a.move_to_element(m).perform()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Nutri-West Products").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//body[1]/main[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/a[1]").click()
    driver.close()
def Prompt_nutriwest():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    driver.maximize_window()

    # Navigate to the website and locate the "Contact Us" link
    driver.get("https://nutriwest.staging.genetechz.com/")  # Replace with the actual URL of the website

    driver.implicitly_wait(10)

    # Find the signup link and open it in a new tab
    signup_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign In As Provider')]")
    signup_link.click()

    # Switch to the new window/tab
    #driver.switch_to.window(driver.window_handles[1])

    # Wait for some time
    driver.implicitly_wait(5)  # Wait for 5 seconds

    # Send email and password and submit the form
    email_input = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")

    email_input.send_keys("gtechprovider@yopmail.com")
    password_input.send_keys("admin123")
    submit_button.click()

    # Wait for terms and conditions page to load, check the checkbox, and submit the button
    time.sleep(5)
    terms_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    terms_checkbox.click()
    terms_submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    terms_submit_button.click()

    # Wait for the navbar to load and hover over the "Products" link
    products_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'products')]")))
    webdriver.ActionChains(driver).move_to_element(products_link).perform()
    time.sleep(2)  # Wait for 2 seconds

    # Find and click the "Nutri-West Products" link from the dropdown
    nutri_west_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Nutri-West Products')]")
    nutri_west_link.click()

    # Wait for the page to load, find the product with slug "product/1-ad-tincture", and click it
    #WebDriverWait(driver, 10).until(EC.url_contains("nutri-west-products"))
    product_link = driver.find_element(By.XPATH, "//a[contains(@href,'products/1-ad-tincture')]")
    product_link.click()

    # Wait for the product page to load, find the "Add to cart" link, and click it
    #WebDriverWait(driver, 10).until(EC.url_contains("product/1-ad-tincture"))

    # Find and click the "Add to Cart" link
    add_to_cart_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Add to Cart')]")
    add_to_cart_link.click()



    # Click the cart in the navbar using the slug in the href
    cart_link = driver.find_element(By.XPATH, "//a[contains(@href, 'cart')]")
    cart_link.click()

    # Close the browser
    driver.quit()
def multiple():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    driver.maximize_window()

    # Navigate to the website and locate the "Contact Us" link
    driver.get("https://nutriwest.staging.genetechz.com/")  # Replace with the actual URL of the website

    # Find and open the signup link in a new tab
    signup_link = driver.find_element(By.XPATH,"//a[contains(text(), 'Sign In As Provider')]")
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).click(signup_link).key_up(Keys.CONTROL).perform()

    # Switch to the new window
    driver.switch_to.window(driver.window_handles[-1])
    driver.implicitly_wait(10)  # Wait for 10 seconds for the page to load

    # Send email and password to the form
    email_input = driver.find_element(By.NAME,"email")
    email_input.send_keys("gtechprovider@yopmail.com")
    password_input = driver.find_element(By.NAME,"password")
    password_input.send_keys("admin123")
    submit_button = driver.find_element(By.XPATH,"//input[@type='submit']")
    submit_button.click()

    # Wait for some time to process the form
    driver.implicitly_wait(5)

    # Check the terms and conditions checkbox and submit the form
    terms_checkbox = driver.find_element(By.XPATH,"//input[@type='checkbox']")
    terms_checkbox.click()
    submit_button = driver.find_element(By.XPATH,"//input[@type='submit']")
    submit_button.click()

    # Wait for some time before performing the next action
    driver.implicitly_wait(5)

    # Hover over the "Products" link in the navbar
    products_link = driver.find_element(By.XPATH,"//a[contains(@href, 'products')]")
    action = ActionChains(driver)
    action.move_to_element(products_link).perform()

    # Wait for the dropdown to appear
    driver.implicitly_wait(5)

    # Find and click the "Nutri-West Products" link
    nutri_west_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Nutri-West Products')]")
    nutri_west_link.click()

    # Wait for some time before performing the next action
    driver.implicitly_wait(5)

    # List of product URLs
    product_urls = ["products/1-ad-tincture", "products/12-ur-kid-herbal"]

    # Loop through the product URLs
    for url in product_urls:
        # Find and click the product link using the slug
        product_link = driver.find_element(By.XPATH,"//a[contains(@href, '{}')]".format(url))
        product_link.click()

        # Wait for some time before performing the next action
        driver.implicitly_wait(5)

        # Find and click the "Add to Cart" link using link_text
        add_to_cart_link = driver.find_element(By.LINK_TEXT,"Add to Cart")
        add_to_cart_link.click()

        # Wait for some time before performing the next action
        driver.implicitly_wait(5)

        # Go back to the Nutri-West Products page
        driver.back()

        # Wait for some time before performing the next action
        driver.implicitly_wait(5)

    # Click the cart link in the navbar
    cart_link = driver.find_element(By.XPATH,"//a[contains(@href, 'cart')]")
    cart_link.click()

    # Close the browser
    driver.quit()


multiple()