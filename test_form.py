from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email # added validators to project

class MyForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()]) # validator to check data is present
    email = StringField('Email', validators=[DataRequired(), Email()]) # validator to checkta is present and email is in correct format.
    submit = SubmitField('Submit')
