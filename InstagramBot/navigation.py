from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def hide_notification_popup(driver):
    WebDriverWait(driver, 60).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//button[text()="Şimdi Değil"]')))

    driver.find_element(By.XPATH, '//button[text()="Şimdi Değil"]').click()

def hide_notification_2_popup(driver):
    WebDriverWait(driver, 60).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//button[text()="Şimdi Değil"]')))

    driver.find_element(By.XPATH, '//button[text()="Şimdi Değil"]').click()
