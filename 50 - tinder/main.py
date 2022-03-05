from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import os


URL = "https://tinder.com/"
USER = os.environ["USER"]
PW = os.environ["PW"]

s = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(URL)

# - - - - - - - - - - S T A R T - - - - - - - - - -

login_btn = driver.find_element(By.LINK_TEXT, "Anmelden")
login_btn.click()
time.sleep(1)

google_btn = driver.find_element(By.XPATH, "//button[@aria-label='Mit Facebook anmelden']")
google_btn.click()
time.sleep(2)

# - - - - - - - - - - L O G I N - - - - - - - - - -

base_window = driver.window_handles[0]
login_window = driver.window_handles[1]
driver.switch_to.window(login_window)
time.sleep(1)

edit_cookie_btn = driver.find_element(By.XPATH, "//button[@title='Weitere Optionen']")
edit_cookie_btn.click()
time.sleep(1)

submit_cookie_btn = driver.find_element(By.XPATH, "//button[@title='Nur erforderliche Cookies erlauben']")
submit_cookie_btn.click()
time.sleep(1)

email_inp = driver.find_element(By.CSS_SELECTOR, "#email")
email_inp.send_keys(USER)

pw_inp = driver.find_element(By.CSS_SELECTOR, "#pass")
pw_inp.send_keys(PW)
time.sleep(1)

pw_inp.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
time.sleep(5)

# - - - - - - - - - - T I N D E R - - - - - - - - - -

location_btn = driver.find_element(By.XPATH, "//button[@aria-label='Zulassen']")
location_btn.click()
time.sleep(1)

notification_btn = driver.find_element(By.XPATH, "//button[@aria-label='Kein Interesse']")
notification_btn.click()

# cookies_btn = driver.find_element(By.XPATH, "//div/div[2]/div/div/div[1]/button/")
# cookies_btn.click()

# - - - - - - - - - - S W I P E - - - - - - - - - -

while True:
    try:
        name = driver.find_element(By.XPATH, "//span[@itemprop='name']").get_attribute("innerHTML").splitlines()[0]
        print("name: " + name)
        img = driver.find_element(By.XPATH, f"//div[@aria-label='{name}']")

        webdriver.ActionChains(driver).drag_and_drop_by_offset(img, 200, 0).perform()

        #like_btn = driver.find_element(By.XPATH, "//button[@class='Bgc($c-like-green):a']")
        # like_btn = driver.find_element(By.XPATH, "//*[@id='c-1420294622']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button")
        # "//*[@id="c-1420294622"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[4]/button"
        # like_btn.click()
    except NoSuchElementException:
        print("element not found")
    time.sleep(2)

driver.quit()