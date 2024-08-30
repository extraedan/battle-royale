from flask import Flask, render_template, request
from sqlalchemy.orm import DeclarativeBase

from forms import InputCharacter
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Character
from characters import Character
# cCREATE FLASK SERVEr
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
bootstrap = Bootstrap(app)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///battle_royale.db'
db.init_app(app)
migrate = Migrate(app, db)

# CREATE LIST OF CHARACTER DICTIONARIES
# Later I can make dynamic so multiple characters
characters = [None, None, None, None]


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/create', methods=['GET', 'POST'])
def choose_characters():
    # //TODO Render each form separately
    form = InputCharacter()
    if request.method == 'POST' and form.validate_on_submit():
        create_edit_character(form)
    return render_template("choose_characters.html", form=form, characters=characters)


def create_edit_character(form):
    index = int(form.slot.data)
    name = form.name.data

    # if nobody in slot, create a new character object
    if characters[index] is None:
        characters[index] = Character(name)
    # if it already exists, just change the attribute
    else:
        characters[index].name = name

if __name__ == '__main__':
    app.run(debug=True)