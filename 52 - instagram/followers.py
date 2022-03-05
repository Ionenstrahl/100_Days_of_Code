from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
import os


# Website
CHROME_DRIVER = "C:\Development\chromedriver.exe"
WEBSITE = "https://www.instagram.com/"

# Login
SIMILAR_ACC = "wizards_magic"
USER = os.environ["USER"]
PW = os.environ["PW"]


class InstaFollowers:

    def __init__(self):
        s = Service(CHROME_DRIVER)
        self.driver = webdriver.Chrome(service=s)

    def login(self):
        self.driver.get(WEBSITE)

        cookies_cond = ec.presence_of_element_located((By.XPATH, "//button[text()='Alle annehmen']"))
        cookies_btn = WebDriverWait(self.driver, 10).until(cookies_cond)
        cookies_btn.click()

        user_cond = ec.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        user_inp = WebDriverWait(self.driver, 10).until(user_cond)
        user_inp.send_keys(USER)

        pw_inp = self.driver.find_element(By.XPATH, "//input[@name='password']")
        pw_inp.send_keys(PW)
        pw_inp.send_keys(Keys.ENTER)

        for i in range(2):
            save_login_cond = ec.presence_of_element_located((By.XPATH, "//button[text()='Jetzt nicht']"))
            save_login_btn = WebDriverWait(self.driver, 10).until(save_login_cond)
            save_login_btn.click()
            if i == 1:
                time.sleep(2)

    def find_followers(self):
        search_cond = ec.presence_of_element_located((By.XPATH, "//input[@aria-label='Sucheingabe']"))
        search_inp = WebDriverWait(self.driver, 10).until(search_cond)
        search_inp.send_keys(SIMILAR_ACC)
        time.sleep(3)
        search_inp.send_keys(Keys.ENTER)
        search_inp.send_keys(Keys.ENTER)

        followers_cond = ec.presence_of_element_located((By.XPATH, f"//a[@href='/{SIMILAR_ACC}/followers/']"))
        followers_link = WebDriverWait(self.driver, 10).until(followers_cond)
        followers_link.click()

        for i in range(5):
            time.sleep(2)
            followers_pop = self.driver.find_element(By.XPATH, "//div[@aria-label='Follower']//a")
            followers_pop.send_keys(Keys.END)

    def follow(self):
        follow_btns = self.driver.find_elements(By.XPATH, "//button[div/text()='Folgen']")
        for follow_btn in follow_btns:
            try:
                self.driver.execute_script("arguments[0].click()", follow_btn)
            except ElementClickInterceptedException:
                cancel_cond = ec.presence_of_element_located((By.XPATH, "//button[text()='Abbrechen']"))
                cancel_btn = WebDriverWait(self.driver, 10).until(cancel_cond)
                cancel_btn.click()
            finally:
                time.sleep(1)
