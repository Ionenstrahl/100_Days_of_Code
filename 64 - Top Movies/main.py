from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# - - - - - - - - - DB with SQLAlchemy - - - - - - - - -
# define table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=250)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(250), nullable=250)
    img_url = db.Column(db.String(250), nullable=250)

    def __repr__(self):
        return f"{self.title}"


# db.drop_all()   # delte all tables
# db.create_all() # create defined table (only needed once)
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


# - - - - - - - - - W T F O R M - - - - - - - - -
class AddForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


# - - - - - - - - - A P I   R E Q U E S T - - - - - - - - -
key = os.environ.get("API_KEY")
url = "https://api.themoviedb.org/3/search/movie"


def get_movie_infos(title: str):
    payload = {
        "api_key": key,
        "query": title,
        "include_adult": True
    }
    r = requests.get(url, params=payload)
    print(r.json()["results"])
    data = r.json()["results"][0]
    print(data)
    """
    hier muss es doch eine schöne Lösung geben
    """
    infos = {}
    infos["img_url"] = "https://image.tmdb.org/t/p/original" + data["poster_path"]
    infos["description"] = data["overview"]
    infos["year"] = data["release_date"][:4]
    return infos


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        movie_to_delete = Movie.query.get(request.form["id"])
        print(movie_to_delete)
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect(url_for("home"))
    print("home")
    top_movies = Movie.query.order_by("rating").limit(10).all()
    for i in range(len(top_movies)):
        top_movies[i].ranking = len(top_movies) - i
    return render_template("index.html", movies=top_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        movie_id = request.form["id"]
        movie_to_edit = Movie.query.get(movie_id)
        movie_to_edit.rating = request.form["rating"]
        movie_to_edit.review = request.form["review"]
        db.session.commit()
        return redirect(url_for("home"))
    movie_id = request.args.get("id")
    movie_to_edit = Movie.query.get(movie_id)
    return render_template("edit.html", movie=movie_to_edit)


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    # Note that you don’t have to pass request.form to Flask-WTF; it will load automatically.
    # And the convenient validate_on_submit will check if it is a POST request and if it is valid.
    if add_form.validate_on_submit():
        title = add_form.title.data
        infos = get_movie_infos(title)

        new_movie = Movie(
            title=title,
            year=infos["year"],
            description=infos["description"],
            rating=0,
            ranking=10,
            review="My favourite character was the caller.",
            img_url=infos["img_url"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html", form=add_form)


if __name__ == '__main__':
    app.run(debug=True)
