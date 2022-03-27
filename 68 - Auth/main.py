from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


## takes users unicode ID and returns user object.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        pw = request.form["password"]
        email = request.form["email"]
        name=request.form["name"]

        if User.query.filter_by(email=email).first():
            flash("Email already registered")
            return redirect(url_for("login"))

        hash_result = generate_password_hash(pw,
                                           method='pbkdf2:sha256',
                                           salt_length=8)
        """
        method, salt, hashed_pw = hash_result.split("$")
        not needed, as eveything is saved in on str :(
        """
        user = User(
            email=email,
            password=hash_result,
            name=name
        )
        db.session.add(user)
        db.session.commit()
        return render_template("secrets.html", user=user)
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"];
        pw = request.form["password"];
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, pw):
            login_user(user)
            return redirect(url_for("secrets"))
        flash("Wrong Credentials")
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    default_user = User(
            email="j@w.de",
            password="asdf",
            name="Jonas"
        )
    return render_template("secrets.html", user=default_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory("static", "files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
