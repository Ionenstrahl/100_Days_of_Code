import time
from bs4 import BeautifulSoup
import requests
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

FORM_URL = os.environ["FORM"]
IMMO_URL = "https://www.immobilienscout24.de/?seaid=g_brand&gclid=CjwKCAiAx8KQBhAGEiwAD3EiPydOxHfV0eCwbu1M9Bhqydsw07Na17s1r3Im_bXWPATGqTbysehSSxoCmowQAvD_BwE"

# Scrap Zillow for flats
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url=IMMO_URL, headers=header)
content = response.text
soup = BeautifulSoup(content, "html.parser")

addresses = soup.select("div[title='Kaltmiete']")
prices = soup.select("a[aria-label='Suchergebnis:*']")
links = soup.select("address")
print(len(prices), len(addresses), len(links))

# dont understand why no html objects are found.