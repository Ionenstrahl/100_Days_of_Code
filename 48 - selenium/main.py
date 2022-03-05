from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# docu https://selenium-python.readthedocs.io/locating-elements.html
s = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.amazon.de/Pegasus-Spiele-57600G-Everdell-deutsche/dp/B084BJBYS1/ref=sr_1_2?crid=2SPZ9SJTQTONX&keywords=everdell&qid=1644002499&sprefix=everdell%2Caps%2C138&sr=8-2")

price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)

title = driver.find_element(By.ID, "productTitle")
print(title.text)

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.text)

# driver.find_element(By.CSS_SELECTOR, ".classname a")


# driver.close() # tab
# driver.quit() # browser

while True:
    pass