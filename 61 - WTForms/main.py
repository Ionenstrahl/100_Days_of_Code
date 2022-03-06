from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = 'a random string'
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


"""
516. WTF Angela? Why do you try to put an hraf into an button -> did not work
"""
"""
521. super(), hat den lila hintergrund überschrieben - nur die überschrift ist rot
"""
@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        return render_template('denied.html')
    return render_template('login.html', form=login_form)


@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')


if __name__ == '__main__':
    app.run(debug=True)