from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# docu https://selenium-python.readthedocs.io/locating-elements.html
s = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://de.wikipedia.org/")

# page_count = driver.find_element(By.XPATH, "//a[@title='Spezial:Statistik']")
# print(page_count.text)

# sign_in = driver.find_element(By.LINK_TEXT, "Anmelden")
# sign_in.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
time.sleep(0.1)
search.send_keys(Keys.ENTER)

while True:
    pass