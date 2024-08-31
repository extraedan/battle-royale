from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import DeclarativeBase

from forms import InputCharacter, NextEvent
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from characters import Character

# Create Flask Server
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
bootstrap = Bootstrap(app)

# //TODO: Create a function that generates list based on number of characters selected
# Create list of character objects
# We start with None so that the indexes already exist, acting as 'slots' for the character objects to fill in
characters = [None, None, None, None]


# //TODO: Create a game route that displays initial characters + events, the game loop, maybe in different file

@app.route('/game', methods=['GET', 'POST'])
def play():
    form = NextEvent()
    return render_template("game.html", characters=characters, form=form)

@app.route('/')
def home():
    return render_template("index.html")

# //TODO: Allow user to select number of characters, make everything dynamic
@app.route('/create', methods=['GET', 'POST'])
def choose_characters():
    # creates four forms
    # //TODO: Make dynamic according to number
    forms = [InputCharacter() for _ in range(4)]

    # if one of the forms is valid, create/edit character and break
    if request.method == 'POST':
        for form in forms:
            if form.validate_on_submit():
                create_edit_character(form)
                return redirect(url_for('choose_characters'))
    # //TODO: Update choose_characters.html to be dynamic according to number
    return render_template("choose_characters.html", forms=forms, characters=characters)


def create_edit_character(form):
    """Creates a new character object or changes the name of an existing character object"""
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