from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MyForm(FlaskForm):
    username = StringField('User Name')
    submit = SubmitField('Submit')
