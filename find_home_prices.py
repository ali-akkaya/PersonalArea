import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


address = '711 Kegley Trestle Rd, Princeton, WV, 24740'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def website_1():
    driver.get('https://www.realtor.com/myhome')
    submission_box = driver.find_element(by=By.XPATH, value='//*[@id="searchbox-input"]')
    submission_box.send_keys(address)
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[3]/div/div[2]/div/div[2]/div[2]/div/div/form/div/button')
    time.sleep(1)
    submit_button.click()
    time.sleep(3)
    popup = driver.find_element(by=By.CLASS_NAME, value='modal-dialog modal-dialog-open')
    claim_button = popup.find_element(by=By.CLASS_NAME, value='rui__ermeke-1 jiNVxF styles__ClaimButton-sc-jw4eu2-21 kbgOIa')
    claim_button.click()

website_1()