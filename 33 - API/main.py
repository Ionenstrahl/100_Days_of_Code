import datetime
import math
import requests
import smtplib
import time
import os


# ----------------- My mail -----------------
my_email = os.environ["EMAIL"]
password = os.environ["PW"]
test_mail = os.environ["TEST_MAIL"]  # smtp "smtp.web.de"


# ----------------- My coords -----------------
# from https://www.latlong.net/ for Cologne
MY_LAT = 50.937531
MY_LONG = 6.960279
VIEW_RANGE = 5


# ----------------- ISS above ? -----------------
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def rel_pos_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    return iss_lat-MY_LAT, iss_lng-MY_LONG


# ----------------- Dark Sky?  -----------------


def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    rise_dt = datetime.datetime.strptime(sunrise, '%Y-%m-%dT%H:%M:%S+00:00')
    set_dt = datetime.datetime.strptime(sunset, '%Y-%m-%dT%H:%M:%S+00:00')

    time_now = datetime.datetime.now()

    if time_now < rise_dt or set_dt < time_now:
        return True
    return False


# ----------------- Visibility Checks  -----------------
while True:
    pos = rel_pos_iss()
    dist = math.sqrt(pos[0]**2 + pos[1]**2)

    if is_dark() and dist < VIEW_RANGE:
        n_or_s = "North" if pos[0] > 0 else "South"
        e_or_w = "East" if pos[1] > 0 else "West"

        message = f"From: \"{'Astro-Jonas'}\" <{my_email}>\n" \
                  f"To: {target_mail}\n" \
                  f"Subject: ISS Above!\n\n" \
                  f"check the sky {pos[0]} {n_or_s} and {pos[1]} {e_or_w}".encode("utf-8")

        with smtplib.SMTP("smtp.gmail.com") as con:
            con.starttls()
            con.login(user=my_email, password=password)
            con.sendmail(from_addr=my_email,
                         to_addrs=target_mail,
                         msg=message)
    time.sleep(60)
