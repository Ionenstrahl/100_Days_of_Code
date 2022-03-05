from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# docu https://selenium-python.readthedocs.io/locating-elements.html
s = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("fName")

l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("lName")

e_mail = driver.find_element(By.NAME, "email")
e_mail.send_keys("em@i.l")

sign_up = driver.find_element(By.CSS_SELECTOR, "button")
sign_up.click()

while True:
    pass