from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# docu https://selenium-python.readthedocs.io/locating-elements.html
s = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.python.org/")

# funktionert nicht
events = driver.find_elements(By.PARTIAL_LINK_TEXT, "/events/python-events")

# holzhammer
events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')

# beste idee
times = driver.find_elements(By.XPATH, "//div[@class='medium-widget event-widget last']/div/ul/li/time")
# times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
names = driver.find_elements(By.XPATH, "//div[@class='medium-widget event-widget last']/div/ul/li/a")
event_dict = {}
if len(times) == len(names):
    for i in range(len(times)):
        event_dict[i] = {"time": times[i].text, "name": names[i].text}
else:
    print("Sth went wrong: len(dates) != len(events)")

print(event_dict)

while True:
    pass