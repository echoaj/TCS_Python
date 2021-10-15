from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo


class SignUpForm(FlaskForm):

    rules = [InputRequired(), Length(min=3, max=20)]
    username = StringField('Username', validators=rules)

    rules = [InputRequired(), Length(min=3, max=100), Email()]
    email = StringField('Email', validators=rules)

    rules = [InputRequired(), Length(min=4), EqualTo('confirm', message="Password must match confirmed password.")]
    password = PasswordField('Password', validators=rules)
    confirm = PasswordField('Confirm Password')

    submit = SubmitField("Sign up")


class LoginForm(FlaskForm):
    rules = [InputRequired(), Length(min=3, max=100), Email()]
    email = StringField('Email', validators=rules)

    rules = [InputRequired(), Length(min=4)]
    password = PasswordField('Password', validators=rules)

    submit = SubmitField("Sign up");