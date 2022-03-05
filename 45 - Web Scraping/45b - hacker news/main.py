import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts = [article.getText for article in soup.find_all(name="a", class_="titlelink")]
article_links = [article.get("href") for article in soup.find_all(name="a", class_="titlelink")]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_i = article_upvotes.index(max(article_upvotes))

print(article_texts[max_i])
print(article_links[max_i])
print(article_upvotes[max_i])
