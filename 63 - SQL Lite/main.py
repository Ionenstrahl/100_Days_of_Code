from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
import sqlite3


# server
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# - - - - - - DB with sqlite3 - - - - - -
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# create DB
# cursor.execute("CREATE TABLE books ("
#               "id INTEGER PRIMARY KEY, "
#               "title varchar(250) NOT NULL UNIQUE, "
#               "author varchar(250) NOT NULL, "
#               "rating FLOAT NOT NULL)")

# insert row
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


# - - - - - - DB with SQLAlchemy - - - - - -
# define table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"{self.title} - {self.author} - {self.rating}"

# db.drop_all()   # delte all tables
# db.create_all() # create defined table (only needed once)


# - - - - - - R O U T E S - - - - - -

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        book_to_delete = Book.query.get(request.form["id"])
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect( url_for("home") )
    return render_template("index.html", all_books=Book.query.all())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect( url_for("home") )
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_edit = Book.query.get(book_id)
        book_to_edit.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("id")
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)


if __name__ == "__main__":
    app.run(debug=False)
    # Debug mode off, otherwise it will server will restart and try to add a duplicate, thworing:
    #
    # sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: book.title
    # [SQL: INSERT INTO book (title, author, rating) VALUES (?, ?, ?)]
    # [parameters: ('LArly Potter', 'L. K. Rowling', 9.0)]
    # (Background on this error at: https://sqlalche.me/e/14/gkpj)




# - - - - - - - - - S U M M A R Y - - - - - - - - -

# - - - CREATE A New Record - - -
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()
# NOTE: When creating new records, the primary key fields is optional. you can also write:


# - - - READ All Records- - -
# all_books = session.query(Book).all()

# - - - READ A Particular Record By Query - - -
# book = Book.query.filter_by(title="Harry Potter").first()


# - - - UPDATE A Particular Record By Query - - -
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# - - - UPDATE A Record By PRIMARY KEY - - -
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()


# - - - DELETE A Particular Record By PRIMARY KEY - - -
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
