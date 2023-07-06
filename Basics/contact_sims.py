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
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import os

def sims_contact():

    # Set the path to your Chrome WebDriver executable
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://sims.media/")

    driver.find_element(By.XPATH,"//a[@href='#contact'][contains(text(),'Contact Us')]").click()
    time.sleep(10)

    firstname=driver.find_element(By.XPATH, '//*[@id="pie-1-field_7YvL9weIDo-2"]')
    firstname.send_keys("Gabriel")
    time.sleep(2)
    lastname=driver.find_element(By.XPATH,"//input[@id='pie-1-field_uey2M3A102-2']")
    lastname.send_keys("Patrick")
    email=driver.find_element(By.XPATH,"//input[@id='pie-1-field_ZP7DBSSQPR-2']")
    email.send_keys("gab@mailinator.com")
    driver.find_element(By.XPATH,"//input[@id='pie-1-field_ipClkVNDFM-2']").send_keys("company")
    select=Select(driver.find_element(By.XPATH, "//select[@id='pie-1-field_GHIiDFuKO5-2']"))
    select.select_by_visible_text('Podcast Booking')
    msg=driver.find_element(By.XPATH,"//textarea[@id='pie-1-field_f0Mrdc4eIA-2']")
    msg.send_keys("This is a message")
    time.sleep(70)

    driver.find_element(By.XPATH,"//div[contains(@class,'pie-submit-container')]").click()
    time.sleep(3)

def Prompt_steve():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://sims.media/#contact")

    time.sleep(10)
    wait = WebDriverWait(driver, 430)
    # Scroll to the contact form
    contact_form = driver.find_element(By.ID,"pie-form-1")
    driver.execute_script("arguments[0].scrollIntoView(true);", contact_form)

    # Fill out the contact form
    fields = {
        "First Name": "John",
        "Last Name": "Doe",
        "Email": "johndoe@example.com",
        "Company": "SimsMedia",
        "Subject": "Podcast Booking",
        "Message": "This is a test message.",
    }

    for label, value in fields.items():
        if label == "Subject":
            subject_dropdown = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//label[contains('.', 'Subject')]/following-sibling::select"))
            )
            subject_dropdown.send_keys(value)
        elif label == "Message":
            message_textarea = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//label[contains('.', 'Message')]/following-sibling::textarea"))
            )
            message_textarea.clear()
            message_textarea.send_keys(value)
        else:
            field_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, f"//label[contains('.', '{label}')]/following-sibling::input"))
            )
            field_input.clear()
            field_input.send_keys(value)

    # Sleep for 100 seconds before submitting the form
    time.sleep(30)

    # Submit the form
    submit_button = driver.find_element(By.XPATH,"//button[@type='submit']")
    submit_button.click()

    # Close the browser
    driver.quit()


def Prompt_BPA():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://www.bpa-solutions.net/contact-us/")
    time.sleep(3)

    # Fill in the contact form fields
    first_name_input = driver.find_element(By.XPATH,
                                           "//span[contains(., 'First Name')]/following-sibling::input")
    first_name_input.clear()
    first_name_input.send_keys("John")

    last_name_input = driver.find_element(By.XPATH,
                                          "//span[contains(., 'Last Name')]/following-sibling::input")
    last_name_input.clear()
    last_name_input.send_keys("Doe")

    company_input = driver.find_element(By.XPATH,
                                        "//span[contains(., 'Company')]/following-sibling::input")
    company_input.clear()
    company_input.send_keys("ABC Company")

    country_dropdown = driver.find_element(By.XPATH, "//span[contains(., 'Country')]/following-sibling::select")
    country_dropdown.send_keys("United States")  # Replace with the desired country value

    comment_textarea = driver.find_element(By.XPATH, "//span[contains(., 'Comment')]/following-sibling::textarea")
    comment_textarea.clear()
    comment_textarea.send_keys("Hello, I have a question about your products.")

    direct_phone_input = driver.find_element(By.XPATH,
                                             "//span[contains(., 'Direct Phone')]/following-sibling::input")
    direct_phone_input.clear()
    direct_phone_input.send_keys("1234567890")

    business_email_input = driver.find_element(By.XPATH,
                                               "//span[contains(., 'Business E-mail')]/following-sibling::input")
    business_email_input.clear()
    business_email_input.send_keys("john.doe@example.com")

    product_dropdown = driver.find_element(By.XPATH, "//span[contains(., 'Product')]/following-sibling::select")
    product_dropdown.send_keys("Quality + Risk")  # Replace with the desired product value

    # Sleep for 2 seconds before submitting the form
    time.sleep(4)
    terms_checkbox = driver.find_element(By.XPATH,
                                         "//input[@type='checkbox'] and following-sibling::span[contains(., 'Terms')]]")
    driver.execute_script("arguments[0].click();", terms_checkbox)
    time.sleep(5)

    # Locate the Submit button and submit the form
    submit_button = driver.find_element(By.XPATH, "//button[@type='button']")
    driver.execute_script("arguments[0].click();", submit_button)
    # Close the web browser
    time.sleep(5)
    driver.quit()
def BPA_mannual():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://www.bpa-solutions.net/contact-us/")
    time.sleep(3)

    # Fill in the contact form fields
    first_name_input = driver.find_element(By.XPATH,
                                           "//span[contains(., 'First Name')]/following-sibling::input")
    first_name_input.clear()
    first_name_input.send_keys("John")

    last_name_input = driver.find_element(By.XPATH,
                                          "//span[contains(., 'Last Name')]/following-sibling::input")
    last_name_input.clear()
    last_name_input.send_keys("Doe")

    company_input = driver.find_element(By.XPATH,
                                        "//span[contains(., 'Company')]/following-sibling::input")
    company_input.clear()
    company_input.send_keys("ABC Company")

    country_dropdown = driver.find_element(By.XPATH, "//span[contains(., 'Country')]/following-sibling::select")
    country_dropdown.send_keys("United States")  # Replace with the desired country value

    comment_textarea = driver.find_element(By.XPATH, "//span[contains(., 'Comment')]/following-sibling::textarea")
    comment_textarea.clear()
    comment_textarea.send_keys("Hello, I have a question about your products.")

    direct_phone_input = driver.find_element(By.XPATH,
                                             "//span[contains(., 'Direct Phone')]/following-sibling::input")
    direct_phone_input.clear()
    direct_phone_input.send_keys("1234567890")

    business_email_input = driver.find_element(By.XPATH,
                                               "//span[contains(., 'Business E-mail')]/following-sibling::input")
    business_email_input.clear()
    business_email_input.send_keys("john.doe@example.com")

    product_dropdown = driver.find_element(By.XPATH, "//span[contains(., 'Product')]/following-sibling::select")
    product_dropdown.send_keys("Quality + Risk")  # Replace with the desired product value

    # Sleep for 2 seconds before submitting the form
    time.sleep(4)
    terms_checkbox = driver.find_element(By.XPATH,"//input[@type='checkbox'] and following-sibling::span[contains(., 'Terms')]]")
    driver.execute_script("arguments[0].click();", terms_checkbox)
    time.sleep(5)

    # Locate the Submit button and submit the form
    submit_button = driver.find_element(By.XPATH, "//button[@type='button']")
    driver.execute_script("arguments[0].click();", submit_button)
    # Close the web browser
    time.sleep(5)
    driver.quit()
def steve_check():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()

    # Navigate to the website and locate the "Contact Us" link
    driver.get("https://sims.media")  # Replace with the actual URL of the website
    contact_us_link = driver.find_element(By.XPATH, "//a[contains(., 'Contact Us')]")

    # Click on the "Contact Us" link
    contact_us_link.click()

    # Scroll to the form with id "pie-form-1"
    form = driver.find_element(By.ID, "pie-form-1")
    driver.execute_script("arguments[0].scrollIntoView(true);", form)

    # Fill in the contact form fields
    first_name_input = driver.find_element(By.XPATH, "//label[contains(., 'First Name')]/following-sibling::input")
    first_name_input.send_keys("John")

    last_name_input = driver.find_element(By.XPATH, "//label[contains(., 'Last Name')]/following-sibling::input")
    last_name_input.send_keys("Doe")

    email_input = driver.find_element(By.XPATH, "//label[contains(., 'Email')]/following-sibling::input")
    email_input.send_keys("john.doe@example.com")

    company_input = driver.find_element(By.XPATH, "//label[contains(., 'Company')]/following-sibling::input")
    company_input.send_keys("ABC Company")

    subject_dropdown = driver.find_element(By.XPATH, "//label[contains(., 'Subject')]/following-sibling::select")
    subject_dropdown.send_keys("Personal Brand Management")

    message_textarea = driver.find_element(By.XPATH, "//label[contains(., 'Message')]/following-sibling::textarea")
    message_textarea.send_keys("Hello, I have a question about your services.")

    # Sleep for 100 seconds before submitting the form
    time.sleep(30)

    # Locate the Submit button and submit the form
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Close the web browser
    driver.quit()

def NHM_Patient():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://nhmedsupply.com/prescription-order-form/")
    time.sleep(5)
    condition_dropdown = Select(driver.find_element(By.NAME, 'i-am'))
    condition_dropdown.select_by_visible_text("Patient")  # Replace with the desired condition (Patient or Caregiver)

    # Wait for the form fields to appear based on the selected condition
    time.sleep(2)  # Adjust the sleep time as needed

    if condition_dropdown.first_selected_option.text == "Patient":
        time.sleep(2)
        patient_first_name_input = driver.find_element(By.NAME, "patient-first-name")
        patient_first_name_input.send_keys("John")
        time.sleep(2)
        driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/div[6]/p[1]/span[1]/input[1]").send_keys("Patrick")
        time.sleep(2)
        file = driver.find_element(By.XPATH,
                                   '//body[1]/div[2]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/div[21]/p[1]/span[1]/div[1]/input[1]')
        time.sleep(2)
        driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/div[7]/p[1]/span[1]/input[1]").send_keys('05-28-2023')
        list_files=['C:/python-selenium/PythonSelenium/LearningSelenium/Basics/screenshot_2.png','C:/python-selenium/PythonSelenium/LearningSelenium/Basics/screenshot_3.png']
        for i in list_files:
            file.send_keys(i)
        # os.system('C:/Users/danella.patrick/Desktop/autoit/fileupload.exe')
        time.sleep(10)
        driver.close()

def nhm_patient_prompt():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://nhmedsupply.com/prescription-order-form/")


    # Select the condition (Patient or Caregiver) from the dropdown
    condition_dropdown = Select(
        driver.find_element(By.NAME, "i-am"))
    condition_dropdown.select_by_visible_text("Patient")  # Replace with the desired condition (Patient or Caregiver)

    # Wait for the form fields to appear based on the selected condition
    time.sleep(2)  # Adjust the sleep time as needed

    # Fill in the form fields based on the selected condition (Patient)
    if condition_dropdown.first_selected_option.text == "Patient":
        # Fill in Patient details
        patient_first_name_input = driver.find_element(By.NAME, "patient-first-name")
        patient_first_name_input.send_keys("John")

        patient_middle_name_input = driver.find_element(By.NAME, "patient-middle-name")
        patient_middle_name_input.send_keys("M")

        patient_last_name_input = driver.find_element(By.NAME, "patient-last-name")
        patient_last_name_input.send_keys("Doe")

        patient_dob_input = driver.find_element(By.NAME, "patient-dob")
        patient_dob_input.send_keys("01-01-2000")  # Replace with the patient's date of birth

        patient_number_input = driver.find_element(By.NAME, "patient-phone-number")
        patient_number_input.send_keys("1234567890")  # Replace with the patient's phone number

        patient_email_input = driver.find_element(By.NAME, "patient-email-address")
        patient_email_input.send_keys("john.doe@example.com")  # Replace with the patient's email address

        street_address_input = driver.find_element(By.NAME, "street-address")
        street_address_input.send_keys("123 Main St")  # Replace with the patient's street address

        state_dropdown = Select(driver.find_element(By.NAME, "state"))
        state_dropdown.select_by_visible_text("California")  # Replace with the patient's state

        city_input = driver.find_element(By.NAME, "city")
        city_input.send_keys("Los Angeles")  # Replace with the patient's city

        zip_input = driver.find_element(By.NAME, "zip")
        zip_input.send_keys("12345")  # Replace with the patient's ZIP code

        insurance_provider_input = driver.find_element(By.NAME, "insurance-provider")
        insurance_provider_input.send_keys("ABC Insurance")  # Replace with the patient's insurance provider

        insurance_policy_id_input = driver.find_element(By.NAME, "insurance-policy-id")
        insurance_policy_id_input.send_keys("123456789")  # Replace with the patient's insurance policy ID

        # Upload Insurance Card Front And Back Images
        list_files = ['C:/python-selenium/PythonSelenium/LearningSelenium/Basics/screenshot_2.png',
                      'C:/python-selenium/PythonSelenium/LearningSelenium/Basics/screenshot_3.png']

        for i in list_files:
            image_input = driver.find_element(By.XPATH, f"//input[@type='file']")
            image_input.send_keys(i)

    # Fill in the form fields based on the selected condition (Caregiver)
    elif condition_dropdown.first_selected_option.text == "Caregiver":
        # Fill in Contact Person details (same as Patient details with additional fields)
        contact_first_name_input = driver.find_element(By.NAME, "contact-first-name")
        contact_first_name_input.send_keys("Jane")

        contact_last_name_input = driver.find_element(By.NAME, "contact-last-name")
        contact_last_name_input.send_keys("Smith")

        phone_number_input = driver.find_element(By.NAME, "contact-phone-number")
        phone_number_input.send_keys("9876543210")  # Replace with the contact person's phone number

        # Fill in Patient details (same as Patient section)
        patient_first_name_input = driver.find_element(By.NAME, "patient-first-name")
        patient_first_name_input.send_keys("John")

        patient_middle_name_input = driver.find_element(By.NAME, "patient-middle-name")
        patient_middle_name_input.send_keys("M")

        patient_last_name_input = driver.find_element(By.NAME, "patient-last-name")
        patient_last_name_input.send_keys("Doe")

        patient_dob_input = driver.find_element(By.NAME, "patient-dob")
        patient_dob_input.send_keys("01-01-2000")  # Replace with the patient's date of birth

        patient_number_input = driver.find_element(By.NAME, "patient-phone-number")
        patient_number_input.send_keys("1234567890")  # Replace with the patient's phone number

        patient_email_input = driver.find_element(By.NAME, "patient-email-address")
        patient_email_input.send_keys("john.doe@example.com")  # Replace with the patient's email address

        street_address_input = driver.find_element(By.NAME, "street-address")
        street_address_input.send_keys("123 Main St")  # Replace with the patient's street address

        state_dropdown = Select(driver.find_element(By.NAME, "state"))
        state_dropdown.select_by_visible_text("California")  # Replace with the patient's state

        city_input = driver.find_element(By.NAME, "city")
        city_input.send_keys("Los Angeles")  # Replace with the patient's city

        zip_input = driver.find_element(By.NAME, "zip")
        zip_input.send_keys("12345")  # Replace with the patient's ZIP code

        insurance_provider_input = driver.find_element(By.NAME, "insurance-provider")
        insurance_provider_input.send_keys("ABC Insurance")  # Replace with the patient's insurance provider

        insurance_policy_id_input = driver.find_element(By.NAME, "insurance-policy-id")
        insurance_policy_id_input.send_keys("123456789")  # Replace with the patient's insurance policy ID

        # Upload Insurance Card Front And Back Images
        list_files = ['C:/python-selenium/PythonSelenium/LearningSelenium/Basics/screenshot_2.png',
                      'C:/python-selenium/PythonSelenium/LearningSelenium/Basics/screenshot_3.png']

        for i in list_files:
            image_input = driver.find_element(By.XPATH, f"//input[@type='file']")
            image_input.send_keys(i)
            time.sleep(4)

    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()

    # Wait for the submission to be processed
    time.sleep(5)  # Sleep for 5 seconds before closing the browser

    # Close the web browser
    driver.quit()


nhm_patient_prompt()