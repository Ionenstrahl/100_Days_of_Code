import datetime
import requests
import os
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# get current date
today = datetime.date.today()
one_day = datetime.timedelta(days=1)

# api call
url = "https://www.alphavantage.co/query"
function = "TIME_SERIES_DAILY"
api_key = os.environ["AA_KEY"]
params = {
    "function": function,
    "symbol": STOCK,
    "apikey":api_key
}

r = requests.get(url=url, params=params)
data = r.json()

# interpret data
latest_stock_day = today
for i in range(4):  # due to weekends we have to look up to 3 days back
    try:
        latest_price = float(data["Time Series (Daily)"][str(latest_stock_day)]["4. close"])
        break
    except KeyError:
        print(f"EOD Stock for {latest_stock_day} not available yet")
        latest_stock_day -= one_day

day_before_latest_stock_day = latest_stock_day - one_day
for i in range(3):  # due to weekends we have to look up to 3 days back
    try:
        penultimate_price = float(data["Time Series (Daily)"][str(day_before_latest_stock_day)]["4. close"])
        break
    except KeyError:
        print(f"EOD Stock for {day_before_latest_stock_day} not available yet")
        day_before_latest_stock_day = day_before_latest_stock_day - one_day

# alternative
EOD_stock_prices = [item[1]["4. close"] for item in data["Time Series (Daily)"].items()]
latest_price = float(EOD_stock_prices[0])
penultimate_price = float(EOD_stock_prices[1])

price_delta = round(100 * (latest_price - penultimate_price) / penultimate_price, 1)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_url = "https://newsapi.org/v2/everything"
news_api_key = os.environ["N_KEY"]
news_params = {
    "q": COMPANY_NAME,
    "from": str(latest_stock_day - datetime.timedelta(days=7)),
    "to": str(today),
    "sortBy": "relevance",
    "apiKey": news_api_key
}

if price_delta > 5:

    news_r = requests.get(url=news_url, params=news_params)
    news_data = news_r.json()

    titles = []
    links = []
    for i in range(3):
        titles.append(news_data["articles"][i]["title"])
        links.append(news_data["articles"][i]["url"])

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

    account_sid = os.environ["A_SID"]
    auth_token = os.environ["A_KEY"]

    sign = "●"
    if price_delta > 1:
        sign = "🔺"
    if price_delta < 1:
        sign = "🔻"

    for i in range(3):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"{COMPANY_NAME} - {latest_stock_day}: {sign}{abs(price_delta)}%\n"
                 f"{titles[i]}:\n"
                 f"{links[i]}",
            from_="+14157375570",
            to=os.environ["TEL"]
        )


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

