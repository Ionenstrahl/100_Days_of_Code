from flask import Flask, render_template, request
import requests
import smtplib
import os


NPOINT_URL = "https://api.npoint.io/484cdd4325f5a6633426"
posts = []

my_email = os.environ["EMAIL"]
password = os.environ["PW"]
test_mail = os.environ["TEST_MAIL"]


app = Flask(__name__)


def get_posts():
    global posts
    return posts if posts else requests.get(NPOINT_URL).json()


"""
Still get: smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. 
Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials hg11-20020a1709072ccb00b006cee4fb36c7sm2974993ejc.64 - gsmtp')
not clear why
"""
def send_mail(name, mail, tel, msg):

    content = f"Name: {name}" \
              f"Mail: {mail}" \
              f"Tel: {tel}" \
              f"Msg: {msg}"

    message = f"From: \"{'Jonas'}\" <{my_email}>\n" \
              f"To: {test_mail}\n" \
              f"Subject: Python Blog Contact Form\n\n" \
              f"{content}".encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls()
        con.login(user=my_email, password=password)
        con.sendmail(from_addr=my_email,
                     to_addrs=test_mail,
                     msg=message)


@app.route("/")
def home():
    return render_template("index.html", posts=get_posts())


@app.route("/about")
def about():
    return render_template("about.html")

"""
button not clickable
I fixed it by removed "disabled" class
"""
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_mail(name=data["name"],
                  mail=data["email"],
                  tel=data["phone"],
                  msg=data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


"""
sometimes post link has to be clicked 2x in order to redirect
"""
@app.route("/post/<int:num>")
def post(num):
    for p in get_posts():
        print(p["id"])
        if p["id"] == num:
            print(p["body"])
            return render_template("post.html",
                                   title=p["title"],
                                   subtitle=p["subtitle"],
                                   body=p["body"],
                                   author=p["author"],
                                   date=p["date"])


if __name__ == "__main__":
    app.run(debug=True)
