import datetime
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, RadioField, SubmitField, TextAreaField, BooleanField

class SignUpForm(FlaskForm):
    first_name = StringField('first_name')
    last_name = StringField('last_name')
    email = EmailField('email')
    options = RadioField('query')
    textarea = TextAreaField('message')
    checkbox = BooleanField('checkbox')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'


    @app.route("/", methods=["GET", "POST"])    
    def index():
        form = SignUpForm()
        if form.is_submitted():
            result = request.form
            print(result)

        
        return render_template("index.html", form=form)

    return app
