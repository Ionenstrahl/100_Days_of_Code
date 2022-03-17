from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField("Location URL", validators=[DataRequired(), URL()])
    open_time = StringField("Opening Time", validators=[DataRequired()])
    close_time = StringField("Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating",
                                choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
                                validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Rating",
                              choices=["🌐", "🌐🌐", "🌐🌐🌐", "🌐🌐🌐🌐", "🌐🌐🌐🌐🌐"],
                              validators=[DataRequired()])
    power_rating = SelectField("Power Rating",
                               choices=["🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", "a", encoding='utf-8') as f:
            print(form.data)
            print(form["cafe"].data)
            f.write(f"\n"
                    f"{form.cafe.data},"
                    f"{form.location.data},"
                    f"{form.open_time.data},"
                    f"{form.close_time.data},"
                    f"{form.coffee_rating.data},"
                    f"{form.wifi_rating.data},"
                    f"{form.power_rating.data}")
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
