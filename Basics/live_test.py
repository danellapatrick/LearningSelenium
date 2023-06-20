from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
#from seleniumwire import webdriver
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def checking_robots(url):
    time.sleep(4)

    url1 = url + "robots.txt"
    driver.get(url1)
    sitemap = driver.find_element(By.TAG_NAME, 'body').text
    print("The robots result is: ", sitemap)
    time.sleep(4)
def checking_srdb(url):
    time.sleep(4)

    url1 = url + "srdb"
    driver.get(url1)
    time.sleep(3)
    try:
        r = requests.head(url1)
        print("the response of srdb is ",r.status_code)
    # prints the int of the status code. Find more at httpstatusrappers.com :)
    except requests.ConnectionError:
        print("failed to connect")
def checking_wp_content(url):
    time.sleep(4)

    url1 = url + "wp-content/uploads"
    driver.get(url1)
    time.sleep(3)
    try:
        r = requests.head(url1)
        print("the response of wp/content is ", r.status_code)
    # prints the int of the status code. Find more at httpstatusrappers.com :)
    except requests.ConnectionError:
        print("failed to connect")
def checking_links():
    for request in driver.requests:
        if request.response:
            print(
                request.url,
                request.response.status_code,
                request.response.headers['Content-Type']
            )

def page_speed(url):
    driver.get("https://gtmetrix.com/")
    time.sleep(2)
    driver.find_element(By.XPATH,"//body/div[1]/main[1]/article[1]/section[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]").send_keys(url)
    time.sleep(4)
    driver.find_element(By.XPATH,"//button[contains(text(),'Test your site')]").click()
def page_speed1(url):
    driver.get("https://pagespeed.web.dev/")
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='i4']").send_keys(url)
    time.sleep(4)
    driver.find_element(By.XPATH,"//body/c-wiz[1]/div[2]/div[1]/div[2]/form[1]/div[2]").click()
def deadlinked(url):
    driver.get("https://www.deadlinkchecker.com/website-dead-link-checker.asp")
    time.sleep(2)
    text2 = re.search("\.[A-Za-z].+", url)
    text2 = text2.group()
    text = re.search("[A-Za-z].+", text2)
    driver.find_element(By.XPATH, "//input[@id='url']").send_keys(text.group())
    time.sleep(5)
    driver.find_element(By.XPATH,"//button[contains(text(),'check')]").click()
    time.sleep(4)


#chop = webdriver.ChromeOptions()
#chop.add_extension("Free-VPN-for-Chrome-by-1click-VPN-proxy.crx")//input[@id='url']

# create new Chrome driver object with Chrome extension


s = Service(ChromeDriverManager().install())
#if you want to use extnesion then write chrome_options
driver = webdriver.Chrome(service=s)
driver.get("https://kilbylaw.com/")
title= driver.title
url=driver.current_url
print(url)
print(title)
driver.maximize_window()
time.sleep(3)
driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window("secondtab")
time.sleep(2)
checking_robots(url)
driver.switch_to.window(driver.window_handles[0])
driver.execute_script("window.open('about:blank','thirdtab');")
driver.switch_to.window("thirdtab")
time.sleep(2)
checking_srdb(url)
driver.switch_to.window(driver.window_handles[0])
driver.execute_script("window.open('about:blank','fourthtab');")
driver.switch_to.window("fourthtab")
time.sleep(2)
checking_wp_content(url)
driver.switch_to.window(driver.window_handles[0])
driver.execute_script("window.open('about:blank','fifthtab');")
driver.switch_to.window("fifthtab")
time.sleep(2)
page_speed(url)
driver.switch_to.window("fifthtab")
time.sleep(2)
page_speed1(url)
driver.switch_to.window(driver.window_handles[0])
driver.execute_script("window.open('about:blank','sixthtab');")
driver.switch_to.window("sixthtab")
time.sleep(2)
deadlinked(url)



