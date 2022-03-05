from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    user = request.form["username"]
    pw = request.form["password"]
    return f"<h1>user:{user} ,pw:{pw}</h1>"


if __name__ == "__main__":
    app.run(debug=True)

# implementation of contact form -> chap 59
