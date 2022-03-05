import datetime
import random
import smtplib
import os


my_email = os.environ["EMAIL"]
password = os.environ["PW"]
test_mail = os.environ["TEST_MAIL"]  # smtp "smtp.web.de"
quote_file = "quotes.txt"

now = datetime.datetime.now()
now.weekday()

# date_of_birth = datetime.datetime(year=1995, month=12, day=27)

with open(quote_file) as f:
    data = f.readlines()
    rnd_line = data[random.randint(0,len(data)-1)]
    rnd_line = random.choice(data)

if now.day == 0:
    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls() # makes con secure
        con.login(user=my_email, password=password)
        con.sendmail(
            from_addr=my_email,
            to_addrs=test_mail,
            msg=f"Subject:Hello\n\n{rnd_line}")
