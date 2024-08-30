from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.fields.simple import HiddenField
from wtforms.validators import DataRequired, URL

class InputCharacter(FlaskForm):
    name = StringField("Character Name", validators=[DataRequired()])
    slot = HiddenField('Slot')
    submit = SubmitField("Add character")