import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import pprint
import os

FORM_URL = os.environ["FORM_URL"]
ZILLOW_URL = "https://www.zillow.com/heidelberg-pa/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Heidelberg%2C%20PA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.10384956622315%2C%22east%22%3A-80.08110443377686%2C%22south%22%3A40.3845074808951%2C%22north%22%3A40.39683018125659%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A5115%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22min%22%3A100%2C%22max%22%3A1000%7D%2C%22price%22%3A%7B%22min%22%3A26751%2C%22max%22%3A267513%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A15%7D"

# Scrap Zillow for flats
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
}
"""
woher weiß man, dass man den header benutzen soll?
"""
response = requests.get(url=ZILLOW_URL, headers=header)
content = response.text
soup = BeautifulSoup(content, "html.parser")

"""
warum finde ich manchmal preise und manchmal nicht?
"""
addresses = soup.select(".list-card-addr")
# prices = soup.find_all("div", class_="list-card-price")
prices = soup.select(".list-card-price")
links = soup.select(".list-card-info .list-card-link")
print(len(prices), len(addresses), len(links))
print(soup.prettify())

if len(prices) == len(addresses) and len(addresses) == len(links):
    if len(prices) > 0:
        flats = [{
            "address": addresses[i].text,
            "price": prices[i].text.split("+")[0],
            "link": links[i]["href"]
            if "http" not in links[i]["href"]
            else f"https://www.zillow.com{links[i]['href']}"
        } for i in range(len(prices))]

        # Post Flats to Google Docs
        s = Service("C:\Development\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get(FORM_URL)

        for flat in flats:
            time.sleep(2)
            """
            Warum funktioniert die unten stehende Zeile erst nach 10x versuchen ohne was zu ändern
             - sie findet zumindest durchgehend 3 Elemente
            inputs = driver.find_elements(By.XPATH, "//div[div/text()='Meine Antwort']/input")
            unten findet 0 elements
            inputs = driver.find_elements(By.XPATH, "//input[@class='quantumWizTextinputPaperinputInput']")
            """
            time.sleep(2)
            """
            Warum funktioniert cond.rendering nicht und findet nie ein element?
            """
            # inputs_cond = ec.presence_of_element_located((By.XPATH, "//div[div/text()='Meine Antwort']/input"))
            # inputs = WebDriverWait(driver, 10).until(inputs_cond)
            inputs = driver.find_elements(By.XPATH, "//div[div/text()='Meine Antwort']/input")
            inputs[0].send_keys(flat["address"])
            inputs[1].send_keys(flat["price"])
            inputs[2].send_keys(flat["link"])
            time.sleep(1)

            submit = driver.find_element(By.XPATH, "//span[text()='Senden']")
            submit.click()

            next_flat_cond = ec.presence_of_element_located((By.LINK_TEXT, "Weitere Antwort senden"))
            next_flat_btn = WebDriverWait(driver, 10).until(next_flat_cond)
            next_flat_btn.click()
    else:
        print("Error: no flats found")
else:
    print("Error: len of prices, addrs & links do not match")
