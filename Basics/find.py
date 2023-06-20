import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
import pyautogui
import os
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://blue3.genetechz.com/intechanchoring/web/helical-piles/pulldown-microp")

driver.maximize_window()
def find(search_term):
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.CONTROL + 'f')

    # wait for the search bar to appear
    time.sleep(2)

    # enter the search term and press Enter
    search_box = driver.switch_to.active_element
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.ENTER)

    # wait for the search results to appear
    time.sleep(2)

    # find all occurrences of the search term
    matches = driver.find_elements(By.XPATH, "//*[contains(text(), '" + search_term + "')]")

    # take a screenshot for each match
    for match in matches:
        # highlight the match
        driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');",
                              match)
        time.sleep(3)

        # scroll to the match
        driver.execute_script("arguments[0].scrollIntoView();", match)
        time.sleep(3)

        # take a screenshot of the webpage
        #driver.save_screenshot('screenshot_' + str(matches.index(match) + 1) + '.png')
        #print('Screenshot taken for match', matches.index(match) + 1)
        #print(search_term)
        #time.sleep(2)

        # remove the highlight
        driver.execute_script("arguments[0].setAttribute('style', 'border: 0px solid red;');", match)

    # close the search bar
    body.send_keys(Keys.CONTROL + Keys.SHIFT + 'f')


# code to perform ctrl+F
list_words=['AB Chance','Helical Resistance','Hubbell','Atlas','Chance','Chance Foundations']
for i in list_words:
    search_term = i
    find(search_term)


# press Ctrl+F to open the search bar

# close the webdriver
driver.quit()