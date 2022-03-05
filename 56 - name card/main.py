from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# make websites editable: document.body.contentEditable=true
# html template from https://html5up.net/