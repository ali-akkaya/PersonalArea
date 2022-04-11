from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path='/Users/aliakkaya/PycharmProjects/PersonalArea/chromedriver')
driver.get("https://www.instagram.com/")
