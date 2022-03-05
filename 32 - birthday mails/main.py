import datetime
import pandas
import random
import smtplib
import os


my_email = os.environ["EMAIL"]
password = os.environ["PW"]
test_mail = os.environ["TEST_MAIL"]  # smtp "smtp.web.de"
quote_file = "quotes.txt"


now = datetime.datetime.now()
now.weekday()

data = pandas.read_csv("../../private/birthdays.csv")


# iterate
for i in range(len(data)):

    # check if day = day & month = month
    birthday = data[data.index == i]
    if int(birthday.day) == now.day and int(birthday.month) == now.month:

        # pick rnd letter
        letter_no = random.randint(1, 3)

        # read letter
        with open(f"letter_templates/letter_{letter_no}.txt", "r") as l:
            letter = l.read()

            # replace name
            letter = letter.replace("[NAME]", birthday.name.item())
            age = now.year - birthday.year.item()

        # send
        message = f"From: \"{'Jonas'}\" <{my_email}>\n" \
                  f"To: {birthday.email.item()}\n" \
                  f"Subject: {age} Jahre, Alles Gute!\n\n" \
                  f"{letter}".encode("utf-8")

        with smtplib.SMTP("smtp.gmail.com") as con:
            con.starttls()
            con.login(user=my_email, password=password)
            con.sendmail(from_addr=my_email,
                         to_addrs=birthday.email,
                         msg=message)

# alternative
# birthday_dict = {(data_row["day"], data_row["month"]): data_row for (index, data_row) in data.iterrows()}
# if (now.day, now.month) in birthday_dict:
#     pass
