from flask import Flask
import random

# - - - - - - - - - - - - D E C O R A T O R S - - - - - - - - - - - -
def make_bold(f):
    def wrapper():
        return "<b>" + f() + "<b>"
    return wrapper


def make_emphasised(f):
    def wrapper():
        return "<em>" + f() + "<em>"
    return wrapper


def make_underlined(f):
    def wrapper():
        return "<u>" + f() + "<u>"
    return wrapper

# waruum passt angelas antwort https://replit.com/@appbrewery/day-55-1-solution#main.py
# nicht zu ihrer frage https://replit.com/@appbrewery/day-55-1-exercise#README.md
def logging_decorator(f):
    def wrapper(*args, **kwargs):
        print("Name: " + f.__name__)
        for arg in args:
            print("arg: " + arg)
        for key, value in kwargs:
            print("kwarg: " + key + " " + value)
        print("Output: " + f(*args, **kwargs))
        return f(*args, **kwargs)

    return wrapper


# - - - - - - - - - - - - A P P - - - - - - - - - - - -

app = Flask(__name__)
correct_num = random.randint(0, 9)


@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src=https://media0.giphy.com/media/hvLwZ5wmarjnNKEJqq/giphy.gif?cid=790b761180a5a6e1465a79b672ca68d16fe368033b8f2e0c&rid=giphy.gif&ct=g>"


@app.route("/<int:guessed_num>")
def number(guessed_num):
    if guessed_num < correct_num:
        return "<h1 style='color:red'>Too low, try again</h1>" \
               "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"
    if guessed_num > correct_num:
        return "<h1 style='color:purple'>Too high, try again</h1>" \
               "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
    if guessed_num == correct_num:
        return "<h1 style='color:green'>You found me</h1>" \
               "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"


if __name__ == "__main__":
    app.run(debug=True)
