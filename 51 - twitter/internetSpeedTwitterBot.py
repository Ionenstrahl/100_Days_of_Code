from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
PROMISED_DOWN = 1000 #MBPS
PROMISED_UP = 150 #MBPS
SPEED_URL = "https://www.speedtest.net/"
TWITTER_EMAIL = os.environ["USER"]
TWITTER_PW = os.environ["PW"]
TWITTER_URL = "https://twitter.com/"


class InternetSpeedTwitterBot():

    def __init__(self):
        s = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=s)
        self.down = 0.0
        self.up = 0.0


    def get_internet_speed(self):
        self.driver.get(SPEED_URL)

        consent_btn = self.driver.find_element(By.XPATH, "//button[text()='I Consent']")
        consent_btn.click()

        go_btn = self.driver.find_element(By.XPATH, "//span[text()='Go']")
        go_btn.click()
        time.sleep(60)

        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").get_attribute("innerHTML"))
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").get_attribute("innerHTML"))

    def check_slow_internet(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            return True


    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(2)

        # - - - - - - L O G I N - - - - - -
        refuse_cookies_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Unwesentliche Cookies ablehnen']")))
        # refuse_cookies_btn = self.driver.find_element(By.XPATH, "//span[text()='Unwesentliche Cookies ablehnen']")
        refuse_cookies_btn.click()

        login_btn = self.driver.find_element(By.XPATH, "//span[text()='Anmelden']")
        login_btn.click()
        time.sleep(2)

        email_inp = self.driver.find_element(By.XPATH, "//input[@name='text']")
        email_inp.send_keys(TWITTER_EMAIL)
        email_inp.send_keys(Keys.ENTER)
        time.sleep(5)

        pw_inp = self.driver.find_element(By.XPATH, "//input[@name='password']")
        pw_inp.send_keys(TWITTER_PW)
        pw_inp.send_keys(Keys.ENTER)
        time.sleep(2)

        # - - - - - - T W E E T - - - - - -
        tweet = f"Hey Internet Provider, warum ist mein Internet {self.down}down/{self.up}up, obwohl ich für {PROMISED_DOWN}down/{PROMISED_UP}up zahle?"
        tweet_inp = self.driver.find_element(By.XPATH, "//div[@aria-label='Text twittern']")
        tweet_inp.send_keys(tweet)

        tweet_btn = self.driver.find_element(By.XPATH, "//span[text()='Twittern']")
        tweet_btn.click()
