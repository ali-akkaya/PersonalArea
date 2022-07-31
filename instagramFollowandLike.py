import pickle
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import threading



username= "css_indicator"
password = "pyjfyq-neczur-dewhU8"
username_to_follow = "micayazilim"
def launchBrowser():
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.instagram.com")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    return driver


driver = launchBrowser()
time.sleep(2)
email = driver.find_element(by=By.NAME, value = 'username').send_keys(username)
sifre = driver.find_element(by=By.NAME, value = 'password').send_keys(password)
login_button = driver.find_element(by=By.XPATH, value = '//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(5)
credentials = driver.find_element(by=By.XPATH, value='//button[text()="Şimdi Değil"]')


credentials.click()
time.sleep(7)
credentials_2 = driver.find_element(by=By.XPATH, value='//button[text()="Şimdi Değil"]').click()

time.sleep(8)
driver.get("https://www.instagram.com/{}/".format(username_to_follow))
time.sleep(5)
follow = driver.find_element(by=By.XPATH, value='//div[text()="Takip Et"]').click()
time.sleep(4)
driver.get('https://www.instagram.com/p/CSE5T8NKmmw/')
time.sleep(7)
driver.find_elements(by=By.XPATH, value='//button[@class="_abl-"]')[1].click()
time.sleep(5)




