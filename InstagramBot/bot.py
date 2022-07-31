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

import navigation

class InstaBot:
    def __init__(self, username, password, proxy_ip_port):


        self.proxy_ip_port = proxy_ip_port if proxy_ip_port else None
        proxy = Proxy()
        proxy.proxy_type = ProxyType.MANUAL
        proxy.http_proxy = proxy_ip_port
        proxy.ssl_proxy = proxy_ip_port

        capabilities = webdriver.DesiredCapabilities.CHROME
        proxy.add_to_capabilities(capabilities)

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
        self.driver.get("https://www.instagram.com")
        WebDriverWait(self.driver, 60).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button').click()
        print("Login Successful")
        navigation.hide_notification_popup(self.driver)
        navigation.hide_notification_2_popup(self.driver)


    def follow_user(self, user_name_to_follow):
        try:
            self.driver.get("https://www.instagram.com/{}/".format(user_name_to_follow))
            WebDriverWait(self.driver, 60).until(
                expected_conditions.presence_of_element_located((By.XPATH, '//div[text()="Takip Et"]')))

            self.driver.find_element(by=By.XPATH, value='//div[text()="Takip Et"]').click()
        except Exception:
            traceback.print_exc()




