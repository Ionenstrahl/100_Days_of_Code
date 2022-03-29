from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask_gravatar import Gravatar
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)

##GRAVATAR IMG
gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)

##CONFIGURE TABLES
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    # This will act like a List of BlogPost objects attached to each User.
    # The "author" refers to the author property in the BlogPost class.
    blog_posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="author")

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id = Column(Integer, ForeignKey('users.id'))
    # Create reference to the User object, the "posts" refers to the posts protperty in the User class.
    author = relationship("User", back_populates="blog_posts")
    comments = relationship("Comment", back_populates="blog_post")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="comments")
    blog_post_id = Column(Integer, ForeignKey('blog_posts.id'))
    blog_post = relationship("BlogPost", back_populates="comments")
db.create_all()


## takes users unicode ID and returns user object.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


"""
Angela schaut in html nur nach:
{% if current_user.id == 1 %}
Das wirft bei mir einen Fehler, wenn ich nicht eingeloggt bin
"""
def check_admin():
    if current_user and current_user.is_authenticated and current_user.id == int(1):
        return True
    return False


def admin_only(f):
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        if check_admin():
            return f(*args, **kwargs)
        # return abort(403)
        # -> 403 Forbidden: You don't have the permission to access the requested resource.
        #    It is either read-protected or not readable by the server.

        # return f(*args, **kwargs)
        # -> RuntimeError: Working outside of application context.

        return render_template("403.html")
        # -> AttributeError: 'NoneType' object has no attribute 'app'
        # -> https://stackoverflow.com/questions/17206728/attributeerror-nonetype-object-has-no-attribute-app

        # return redirect(url_for("not_authorized"))
        # -> RuntimeError: Attempted to generate a URL without the application context being pushed.
        #    This has to be executed when application context is available.

    return wrapper_function()


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts, is_admin=check_admin())


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        # read form data
        pw = form.password.data
        email = form.email.data
        name = form.name.data

        # check for doubles
        if User.query.filter_by(email=email).first():
            flash("Email already registered")
            return redirect(url_for("login"))

        # check for doubles
        hash_result = generate_password_hash(pw,
                                             method='pbkdf2:sha256',
                                             salt_length=8)

        # add new user
        user = User(
            email=email,
            password=hash_result,
            name=name
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for("get_all_posts"))
    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pw = form.password.data
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, pw):
            login_user(user)
            return redirect(url_for("get_all_posts"))
        flash("Wrong Credentials")
    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    form = CommentForm()
    requested_post = BlogPost.query.get(post_id)
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=form.text.data,
            author=current_user,
            blog_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
    return render_template("post.html", post=requested_post, is_admin=check_admin(), form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=["GET", "POST"])
@login_required
# @admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>")
@login_required
# @admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
@login_required
# @admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/403")
def not_authorized():
    return render_template("403.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
