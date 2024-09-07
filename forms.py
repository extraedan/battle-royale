from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField, IntegerField
from wtforms.fields.simple import HiddenField
from wtforms.validators import DataRequired, URL, NumberRange


class InputCharacter(FlaskForm):
    name = StringField("", validators=[DataRequired()])
    slot = HiddenField('Slot')
    submit = SubmitField("Add character")

class NextEvent(FlaskForm):
    submit = SubmitField("Next event")

class CharacterAmount(FlaskForm):
    amount = IntegerField(
        "Amount",
        validators=[
            DataRequired(message="Please enter a number."),
            NumberRange(min=1, max=12, message="The amount must be between 1 and 12.")
        ]
    )
    submit = SubmitField("Add amount")