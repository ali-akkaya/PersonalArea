import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

username= "alibutstraight"
password = "2sGJ#9JN"
def launchBrowser():
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.instagram.com")
    return driver


driver = launchBrowser()
time.sleep(2)
email = driver.find_element(by=By.NAME, value = 'username').send_keys(username)
sifre = driver.find_element(by=By.NAME, value = 'password').send_keys(password)
login_button = driver.find_element(by=By.XPATH, value = '//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(3)
driver.get("https://www.instagram.com/{}/".format(username))
time.sleep(3)
driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()



