from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, PasswordField, FileField, IntegerField
from wtforms.fields.simple import HiddenField
from wtforms.validators import DataRequired, URL, NumberRange, Length, Regexp, Optional


class InputCharacter(FlaskForm):
    name = StringField("", validators=[
        DataRequired(),
        Length(min=2, max=30, message="Name must be between 2 and 30 characters."),
        Regexp('^[A-Za-z0-9 ]*$', message="Name can only contain letters, numbers, and spaces.")
    ])
    image = FileField('Character Image', validators=[
        Optional(),
        FileAllowed(['jpg', 'png', 'gif'], 'Images only!')
    ])
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