from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    username = StringField('username', validators= [DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit_button = SubmitField()

class MarvelForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    comics_appeared_in = StringField('comics appeared in')
    super_power = StringField('super_power')
    submit_button = SubmitField()

class MarvelForm2(FlaskForm):
    name = StringField('name')
    submit_button = SubmitField()