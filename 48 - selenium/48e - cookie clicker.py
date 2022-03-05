from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
from datetime import timedelta
import time

# docu https://selenium-python.readthedocs.io/locating-elements.html
s = Service("C:\Development\chromedriver.exe")

# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=C:/Users/jonas/AppData/Local/Google/Chrome/User Data")

driver = webdriver.Chrome(service=s)
driver.get("https://orteil.dashnet.org/cookieclicker/")


def buy_first(items):
    if len(items) >= 1:
        items[0].click()
        return True


def buy_expensive(items):
    if len(items) == 1:
        items[0].click()
    elif len(items) > 1:
        items[-1].click()



UPGRADE_FREQUENCY = 1
EASY_MODE = False

time.sleep(1)
start_time = datetime.now()
last_upgrade_time = datetime.now()
cookie = driver.find_element(By.ID, "bigCookie")

# - - - - - - - - - - - - E A S Y   M O D E  - - - - - - - - - - - -
if EASY_MODE:
    while datetime.now() < start_time + timedelta(minutes=5):
        if datetime.now() < last_upgrade_time + timedelta(seconds=UPGRADE_FREQUENCY):
            cookie.click()
        else:
            upgrades = driver.find_elements(By.XPATH, "//div[@id='upgrades']/div[@class='crate upgrade enabled']")
            buy_expensive(upgrades)

            products = driver.find_elements(By.XPATH, "//div[@id='products']/div[@class='product unlocked enabled']")
            buy_expensive(products)

            last_upgrade_time = datetime.now()


# - - - - - - - - - - - - H A R D   M O D E  - - - - - - - - - - - -
if not EASY_MODE:
    phase = 1
    click_str = 0
    ULT_PHASE_DELAY = 5
    ult_phase_ticker = 0
    print("phase 1")
    while datetime.now() < start_time + timedelta(minutes=5):
        if datetime.now() < last_upgrade_time + timedelta(seconds=UPGRADE_FREQUENCY):
            cookie.click()
        else:
            if phase == 1:
                products = driver.find_elements(By.XPATH, "//div[@id='products']/div[@class='product unlocked enabled']")
                buy_first(products)

                cursors_owned = driver.find_element(By.CSS_SELECTOR, "#products .content .owned").text
                if int(cursors_owned) >= 10:
                    phase = 2
                    print("phase 2")

            elif phase == 2:
                upgrades = driver.find_elements(By.XPATH, "//div[@id='upgrades']/div[@class='crate upgrade enabled']")
                if buy_first(upgrades):
                    click_str += 1
                    if click_str == 3:
                        phase = 3
                        print("phase 3")

            elif phase == 3:
                if ult_phase_ticker == 0:
                    upgrades = driver.find_elements(By.XPATH, "//div[@id='upgrades']/div[@class='crate upgrade enabled']")
                    buy_expensive(upgrades)

                    products = driver.find_elements(By.XPATH, "//div[@id='products']/div[@class='product unlocked enabled']")
                    buy_expensive(products)

                ult_phase_ticker += 1
                ult_phase_ticker %= ULT_PHASE_DELAY

            last_upgrade_time = datetime.now()



# war nicht in der lage das element per CSS_SELECTOR oder XPATH zu finden
# <div id="cookies" class="title">
#   4.268 million
#   <br>
#   cookies
#   <div style="font-size:50%;">per second : 2,824</div>
# </div>
# driver.find_element(By.CSS_SELECTOR, "#cookies div")
# driver.find_element(By.XPATH, "//div[@id='cookies']/div")
per_s = driver.find_element(By.ID, "cookies").text.split('\n')[1]
print("5 min - Cookies " + per_s)