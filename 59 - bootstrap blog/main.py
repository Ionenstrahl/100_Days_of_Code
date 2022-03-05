from flask import Flask, render_template
import requests


app = Flask(__name__)

NPOINT_URL = "https://api.npoint.io/484cdd4325f5a6633426"
posts = []


def get_posts():
    global posts
    return posts if posts else requests.get(NPOINT_URL).json()


@app.route("/")
def home():
    return render_template("index.html", posts=get_posts())


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

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
