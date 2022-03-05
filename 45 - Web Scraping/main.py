from bs4 import BeautifulSoup

# import lxml


with open("website.html", encoding="utf-8") as file:
    contents = file.read()


# 399 - Parsing HTML
soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())


# 400 - Finding and Selecting
all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

# search for both
heading = soup.find(name="h1", id="name")
section_heading = soup.find(name="h3", class_="heading")
company_url = soup.select_one(selector="p a")
name = soup.select_one(selector="#name")
headings = soup.select(".heading")

print(headings)
