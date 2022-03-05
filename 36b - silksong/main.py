import datetime
import requests
from twilio.rest import Client
import os

TEL_NRS = os.environ["TEL"]
DAILY_CONTENT = "Silksong"

news_url = "https://newsapi.org/v2/everything"
news_api_key = os.environ["N_KEY"]

news_params = {
    "q": DAILY_CONTENT,
    "from": str(datetime.date.today() - datetime.timedelta(days=1)),
    "to": str(datetime.date.today()),
    "sortBy": "relevance",
    "language": "en",
    "apiKey": news_api_key
}

news_r = requests.get(url=news_url, params=news_params)
news_data = news_r.json()

try:
    title = news_data["articles"][0]["title"]
    description = news_data["articles"][0]["description"]
    link = news_data["articles"][0]["url"]
    content = "\n" + \
              title + ":"\
              "\n" + \
              description + \
              "\n" + \
              link
except IndexError:
    content = "No new content yet. Have a cup of tea and slay some bugs 🐛"

account_sid = os.environ["A_SID"]
auth_token = os.environ["A_KEY"]

for tel_nr in TEL_NRS:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=content,
        from_="+14157375570",
        to=tel_nr
    )

