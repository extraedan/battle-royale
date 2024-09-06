from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField, IntegerField
from wtforms.fields.simple import HiddenField
from wtforms.validators import DataRequired, URL

class InputCharacter(FlaskForm):
    name = StringField("", validators=[DataRequired()])
    slot = HiddenField('Slot')
    submit = SubmitField("Add character")

class NextEvent(FlaskForm):
    submit = SubmitField("Next event")

class CharacterAmount(FlaskForm):
    amount = IntegerField("Amount", validators=[DataRequired()])
    submit = SubmitField("Add amount")