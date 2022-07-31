

import pickle
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import threading

def launchBrowser():
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    #chrome_options.add_argument("--headless")
    chrome_options.headless = True
    #PROXY = "103.4.94.12:8080"
    #chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    #cookies = pickle.load(open("cookies.pkl", "rb"))
    #for cookie in cookies:
     #   driver.add_cookie(cookie)
    return driver



username= "css_indicator"
password = "pyjfyq-neczur-dewhU8"


def follow_people(browser, username_to_follow):

    browser.get("https://www.instagram.com")
    time.sleep(2)
    email = browser.find_element(by=By.NAME, value='username').send_keys(username)
    sifre = browser.find_element(by=By.NAME, value='password').send_keys(password)
    login_button = browser.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button').click()

    time.sleep(5)
    print("Login Successful")
    try:
        credentials = browser.find_element(by=By.XPATH, value='//button[text()="Şimdi Değil"]')
        credentials.click()
    except:
        pass
    time.sleep(7)
    try:

        credentials_2 = browser.find_element(by=By.XPATH, value='//button[text()="Şimdi Değil"]').click()
    except:
        pass
    time.sleep(8)
    browser.get("https://www.instagram.com/{}/".format(username_to_follow))
    time.sleep(15)
    print("Follower finded.")
    follow = browser.find_element(by=By.XPATH, value='//div[text()="Takip Et"]').click()
    time.sleep(4)

driver = launchBrowser()
follow_people(driver, 'artsneedyou')