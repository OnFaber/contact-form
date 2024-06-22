from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    EmailField,
    RadioField,
    SubmitField,
    TextAreaField,
    BooleanField,
)
from wtforms.validators import InputRequired, ValidationError
from models import Contact


class ContactForm(FlaskForm):
    first_name = StringField(
        "first name", validators=[InputRequired(message="field must not be empty")]
    )
    last_name = StringField(
        "last name", validators=[InputRequired(message="field must not be empty")]
    )
    email = EmailField(
        "email",
        validators=[InputRequired(message="please enter a valid email address")],
    )
    options = RadioField(
        "query type",
        choices=[("enquiry", "general enquiry"), ("support", "support request")],
        validators=[InputRequired("please select a query type")],
    )
    textarea = TextAreaField(
        "message", validators=[InputRequired("field must not be empty")]
    )
    checkbox = BooleanField(
        "To submit this form, please consent to being contacted",
        validators=[InputRequired("field must not be empty")],
    )

    def __init__(self, *args, **kwargs):
        self.db_model = kwargs.pop("db_model")
        super().__init__(*args, **kwargs)

    def validate_email(self, email):
        if self.db_model.query.filter_by(email=email.data).first():
            raise ValidationError("please enter a valid email address")
