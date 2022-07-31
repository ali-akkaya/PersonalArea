import traceback

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType

import constants

class InstaBot:
    def __init__(self, username, password,):


        # self.proxy_ip_port = proxy_ip_port if proxy_ip_port else None
        # proxy = Proxy()
        # proxy.proxy_type = ProxyType.MANUAL
        # proxy.http_proxy = proxy_ip_port
        # proxy.ssl_proxy = proxy_ip_port
        #
        # capabilities = webdriver.DesiredCapabilities.CHROME
        # proxy.add_to_capabilities(capabilities)

        self.username = username
        self.password = password
        self.driver = self.launch_browser()
        self.login()

    def launch_browser(self):
        chrome_options = Options()
        chrome_options.add_argument("start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, )
        return driver

    def login(self):
        self.driver.get("https://linktr.ee/login")

        WebDriverWait(self.driver, 60).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/main/div/div[1]/div/button')))
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.password)
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="root"]/div/main/div/div[1]/div/button').click()


        print("Login Successful")



    def add_new_link(self, user_name_to_follow):
        try:

            WebDriverWait(self.driver, 60).until(
                expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="Link--ReactLinkEditor"]/div/div/div/div/div[1]/div/div[1]/div/button')))

            self.driver.find_element(by=By.XPATH, value='//*[@id="Link--ReactLinkEditor"]/div/div/div/div/div[1]/div/div[1]/div/button').click()

        except Exception:
            traceback.print_exc()




