from twilio.rest import Client
import smtplib
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self, data, channel, mails):

        account_sid = os.environ["SID"]
        auth_token = os.environ["TOKEN"]

        for flight in data:
            message = f'Low price alert!\n' \
                      f'Only {flight["price"]} € for 2 persons\n' \
                      f'from {flight["dpr"]} to {flight["dst"]},\n' \
                      f'from {flight["from"]} to {flight["to"]},\n' \
                      f'{flight["link"]}'

            if channel == "console":
                print(message)

            elif channel == "sms":
                client = Client(account_sid, auth_token)
                message = client.messages \
                    .create(
                    body=message,
                    from_="+14157375570",
                    to=os.environ["TEL"]
                )

            elif channel == "mail":
                my_email = os.environ["EMAIL"]
                password = os.environ["PW"]
                for mail in mails:
                    with smtplib.SMTP("smtp.gmail.com") as con:
                        con.starttls()
                        con.login(user=my_email, password=password)
                        con.sendmail(from_addr=my_email,
                                     to_addrs=mail,
                                     msg=message.encode("utf-8"))
