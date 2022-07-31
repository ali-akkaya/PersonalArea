

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
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    #cookies = pickle.load(open("cookies.pkl", "rb"))
    #for cookie in cookies:
     #   driver.add_cookie(cookie)
    return driver




# "css_indicator"
# "pyjfyq-neczur-dewhU8"
username= "indicator_css"
password = "pomzeR-zyzto7-zibxux"

threads = []
userList =['artsneedyou','erenblogger', '4play_people', 'pinar.manavi', 'agucompsociety']
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
    time.sleep(5)
    try:

        credentials_2 = browser.find_element(by=By.XPATH, value='//button[text()="Şimdi Değil"]').click()
    except:
        pass
    time.sleep(5)
    browser.get("https://www.instagram.com/{}/".format(username_to_follow))
    time.sleep(5)
    print("Follower finded.")
    follow = browser.find_element(by=By.XPATH, value='//div[text()="Takip Et"]').click()
    print("Done")


for i in range(5):
    driver = launchBrowser()
    browserThread = threading.Thread(target=follow_people, args=[driver, userList[i]])
    browserThread.start()
    threads.append(browserThread)

for thread in threads:
    thread.join()