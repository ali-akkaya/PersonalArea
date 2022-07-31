import pickle
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def launchBrowser(link):
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("user-data-dir=selenium")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(link)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(1)
    email = driver.find_element(by=By.XPATH, value='// *[ @ id = "username"]').send_keys('gecicinew1')
    time.sleep(2)
    password = driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys('jyhvuX-juxxac-2fomru')
    time.sleep(2)
    login_button = driver.find_element(by=By.XPATH, value='// *[ @ id = "content"] / div[2] / div / div[2] / div / form / table / tbody / tr[3] / td / button').click()
    time.sleep(2)



    return driver

driver = launchBrowser("https://www.planespotters.net/production-list/Airbus/A310?p=1")
time.sleep(15)
#pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
table = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div[3]/div[1]/div')
rows = table.find_elements(by=By.CLASS_NAME, value='dt-tr')
print(len(rows))
rows.pop(0)
print(len(rows))
msi_links =[]

for row in rows:
    link = row.find_elements(by=By.TAG_NAME, value='div')[1].find_element(by=By.TAG_NAME, value='a').get_attribute('href')
    msi_number = row.find_elements(by=By.TAG_NAME, value='div')[1].find_element(by=By.TAG_NAME, value='span').text
    msi_links.append([msi_number,link])

for msi_link in msi_links:
    driver.get(msi_link[1])
    info_table = driver.find_element(by=By.XPATH, value='// *[ @ id = "content"] / div[1] / div / div[1] / div[1]')
    info_rows = info_table.find_elements(by=By.CLASS_NAME, value='dt-tr')
    info_rows.pop(0)
    for info_row in info_rows:
        row_name = info_row.find_elements(by=By.TAG_NAME, value='div')[0].text
        if row_name == 'Aircraft Type':
            sections = info_row.find_elements(by=By.TAG_NAME, value='div')[1].find_elements(by=By.TAG_NAME, value='li')
            print(row_name, sections[0].text, sections[1].text)
        else:
            row_value = info_row.find_elements(by=By.TAG_NAME, value='div')[1].text
            print(row_name, row_value)
    time.sleep(5)

    operator_history = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[2]/div')
    operator_rows = operator_history.find_elements(by=By.CLASS_NAME, value='dt-tr')
    tags =[]
    tag_list = operator_rows[0].find_elements(by=By.TAG_NAME, value='div')
    for tag in tag_list:
        tags.append(tag.text)
    print(tags)
    operator_rows.pop(0)
    for operator_row in operator_rows:
        operration_infos = operator_row.find_elements(by=By.TAG_NAME, value='div')
        print(len(operration_infos))

