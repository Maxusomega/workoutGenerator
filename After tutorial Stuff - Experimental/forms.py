from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SignUpForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email address')
    sport = StringField('Sport (currently only supports "swim")')
        
    submit = SubmitField("Submit")
