import pickle
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import threading
from concurrent.futures import ThreadPoolExecutor

def launchBrowser():
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    #chrome_options.add_argument("--headless")
    #chrome_options.headless = True
    #chrome_options.add_argument("user-agent=Chrome/103.0.5060.53")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)



    return driver

username= "indicator_css"
password = "pomzeR-zyzto7-zibxux"

threads = []
userList =['artsneedyou','kerevizy', 'faoluramadogibiolmaz', 'alibutstraight', 'agugompsociety',]

def follow_people(username_to_follow):
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    # chrome_options.add_argument("--headless")
    # chrome_options.headless = True
    # chrome_options.add_argument("user-agent=Chrome/103.0.5060.53")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("https://www.instagram.com")
    time.sleep(4)
    email = driver.find_element(by=By.NAME, value='username').send_keys(username)
    sifre = driver.find_element(by=By.NAME, value='password').send_keys(password)
    login_button = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button').click()
    time.sleep(5)
    print("Login Successful")
    time.sleep(2)
    try:
        credentials = driver.find_element(by=By.XPATH, value='//button[text()="Şimdi Değil"]')
        credentials.click()
    except:
        pass
    time.sleep(7)
    try:

        credentials_2 = driver.find_element(by=By.XPATH, value='//button[text()="Şimdi Değil"]').click()
    except:
        pass
    time.sleep(8)
    driver.get("https://www.instagram.com/{}/".format(username_to_follow))
    time.sleep(15)
    print("Follower finded.")
    follow = driver.find_element(by=By.XPATH, value='//div[text()="Takip Et"]').click()
    time.sleep(4)

    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')


with ThreadPoolExecutor(max_workers=5) as executor:
    for  name in userList:
        future = executor.submit(follow_people, name)
#
# for i in range(5):
#     driver = launchBrowser()
#     browserThread = threading.Thread(target=follow_people, args=[driver, userList[i]])
#     browserThread.start()
#     threads.append(browserThread)
#
# for thread in threads:
#     thread.join()