from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired, URL

class InputCharacter(FlaskForm):
    image = FileField('Character Image')
    title = StringField("Character Name", validators=[DataRequired()])