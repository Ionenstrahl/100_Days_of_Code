import requests
from bs4 import BeautifulSoup

WISH_PRICE = 50
EVERDELL_URL = "https://www.amazon.de/Game-Salute-GSUH2600-Everdell-English/dp/B0792JY6G4/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=DU0YPCCCQW1Q&keywords=everdell&qid=1643918662&sprefix=everdell%2Caps%2C90&sr=8-1"
# hier habe ich nachgescahut, da ich ohne den hint nicht drauf gekommen bin einen header hinzuzufügen
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}

response = requests.get(url=EVERDELL_URL, headers=header)

soup = BeautifulSoup(response.text, "html.parser")

# hier habe ich nur find_all() versucht, das find habe aus der Lösung
price = soup.find(class_="a-offscreen").get_text()

# eine Idee, wie Ihre Lösung klappen soll habe ich nicht
cents = int(price[-3:-1])
euros = int(price[:-4])
price_as_float = euros + 0.01 * cents

if price_as_float < WISH_PRICE:
    print("congrats lad, better buy everdell")
else:
    print(f"Na, better dont buy.\nFor {price_as_float} you could buy a whole castle")
