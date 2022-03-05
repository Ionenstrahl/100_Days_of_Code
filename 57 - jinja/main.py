from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

CURRENT_YEAR = datetime.datetime.now().year
MY_NAME = "Jonas"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
}
GENDERIZE_URL = "https://api.genderize.io"
AGIFY_URL = "https://api.agify.io"
NPOINT_URL = "https://api.npoint.io/87df44b4543c6c25715c"
blog_posts = []


def fetch_blog():
    global blog_posts
    if blog_posts:
        return blog_posts
    blog_r = requests.get(NPOINT_URL)
    blog_posts = blog_r.json()
    return blog_posts


@app.route("/")
def home():
    return render_template("index.html", year=CURRENT_YEAR, name=MY_NAME)


@app.route("/guess/<name>")
def get_guess(name):
    gender_r = requests.get(f"{GENDERIZE_URL}?name={name}")
    age_r = requests.get(f"{AGIFY_URL}?name={name}")
    return render_template("guess.html",
                           guess_name=name.capitalize(),
                           gender=gender_r.json()["gender"],
                           age=age_r.json()["age"],
                           year=CURRENT_YEAR,
                           name=MY_NAME)


@app.route("/blog")
def get_blog():
    return render_template("blog.html",
                           blog_json=fetch_blog(),
                           year=CURRENT_YEAR,
                           name=MY_NAME)


@app.route("/post/<int:num>")
def get_post(num):
    for blog_post in fetch_blog():
        if blog_post["id"] == num:
            return render_template("post.html",
                                   blog_post=blog_post,
                                   year=CURRENT_YEAR,
                                   name=MY_NAME)


if __name__ == "__main__":
    app.run(debug=True)

