from flask import Flask

app = Flask(__name__)

# https://flask.palletsprojects.com/en/1.1.x/quickstart/
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# warum kann ich keine env Variablen setzten und den server starten
# set FLASK_APP=hello
# flask run

if __name__ == "__main__":
    app.run()