import requests
import os
from twilio.rest import Client


# twilio credentials
account_sid = os.environ["SID"]
auth_token = os.environ["TOKEN"]


# cologne pos
cgn_lat = 50.935173
cgn_lon = 6.953101


# weather api
url = "https://api.openweathermap.org/data/2.5/onecall"
exclude = "current,alerts,minutely,daily" # "current,minutely,daily,alerts"
api_key = os.environ["KEY"]

weather_params = {
    "lat": cgn_lat,
    "lon": cgn_lon,
    "appid": api_key,
    "exclude": exclude,
}

response = requests.get(url=url, params=weather_params)
data = response.json()


# check weather and send sms
# weather condition-codes: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
for i in range(12):

    # check for fog
    if data["hourly"][i]["weather"][0]["id"] == 741:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="Fog inc 🌫️",
            from_="+14157375570",
            to=os.environ["TEL"]
        )
        break

    # check for rain
    if data["hourly"][i]["weather"][0]["id"] < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It's gonna be raining today 🌧️",
            from_="+14157375570",
            to=os.environ["TEL"]
        )
        break
