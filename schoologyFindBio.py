import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# To use this app you need to add your own email and password.
# Also, you need to add your own driver path.
# To search for a bio, you need to change bio_info to the bio you want to search for.
# All users will be checked and when it finds the bio, it will print the 'BIO IS FOUND' message.


email = 'YOUR_EMAIL'
password = 'YOUR_PASSWORD'
bio_info = 'YOUR_BIO'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def login_to_schoology(email, password):
    driver.get('https://agu.schoology.com/login?&school=49890877')

    email_box = driver.find_element(by=By.NAME, value='mail')
    email_box.send_keys(email)

    password_box = driver.find_element(by=By.NAME, value='pass')
    password_box.send_keys(password)

    login_button = driver.find_element(by=By.NAME, value='op')
    login_button.click()


def search_for_specific_bio(bio_info):
    # After login, we need to go to the members page.
    driver.get('https://agu.schoology.com/group/65783683/members')

    # Since there are 952 students and each page has 30 students, we need to search by 30 by 30
    # This code opens students info page and searches for the bio. You can customize it.
    for j in range(1, 33):
        for i in range(1, 31):
            user = driver.find_element(by=By.XPATH, value='//*[@id="roster-wrapper"]/div/div/div/div['
                                                          '1]/table/tbody/tr[{}]/td[2]/a'.format(i))
            link = user.get_attribute('href')
            driver.execute_script("window.open('');")
            # Switch to the new window
            driver.switch_to.window(driver.window_handles[1])
            driver.get(link)
            time.sleep(3)
            user_name = driver.find_element(by=By.XPATH,
                                            value='/html/body/div[1]/div[3]/div[1]/div[2]/div/div/div[1]/h2')
            print(user_name.text)
            try:
                text = driver.find_element(by=By.XPATH,
                                           value='/html/body/div[1]/div[3]/div[1]/div[2]/div/div/div[2]/div/div['
                                                 '1]/div/table/tbody/tr[2]/th').text
                if text == "Bio":
                    print("Bio is there")
                    bio = driver.find_element(by=By.XPATH,
                                              value='/html/body/div[1]/div[3]/div[1]/div[2]/div/div/div[2]/div/div['
                                                    '1]/div/table/tbody/tr[2]/td')
                    print(bio.text)
                    if bio.text == bio_info:
                        print("BIO IS FOUND")
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        break
                else:
                    print("Bio is not there")
            except Exception as e:
                print("Bio is not there exception", e.__class__)
            print()
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(0.2)
        next_button = driver.find_element(by=By.XPATH,
                                          value='/html/body/div[1]/div[3]/div[1]/div[2]/div/div/div['
                                                '2]/div/div/div/div/div/div/div/div[2]/div[3]')
        next_button.click()
        time.sleep(2)  # Wait for page to load.


login_to_schoology(email, password)
search_for_specific_bio(bio_info)
