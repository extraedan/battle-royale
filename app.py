from flask import Flask, render_template, request, redirect, url_for
from forms import InputCharacter, NextEvent
from flask_bootstrap import Bootstrap
from characters import Character
from events import events
from anthropic_shenanagins import create_input_message
import random

# Create Flask Server
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
bootstrap = Bootstrap(app)

# //TODO: Create a function that generates list based on number of characters selected
# Create list of character objects
# We start with None so that the indexes already exist, acting as 'slots' for the character objects to fill in
characters = [None, None, None, None]


def generate_event():
    print("You have entered generate event function")
    # each round, make a list of living characters
    events_to_display = []
    character_pool = [character for character in characters if character.death == 0]
    print(character_pool)

    # go through each character in the pool
    print("You are starting to iterate")
    for character in character_pool:
        print("working step 1")
        # define and remove from pool char_a
        char_a = character
        char_b = None # default value for char_b unless overridden
        character_pool.remove(char_a)

        # 50% chance another character is involved
        # define and remove from pool char_b
        if random.choice([True, False]) and len(character_pool) > 1:
            char_b = random.choice(character_pool)
            character_pool.remove(char_b)

        # create input message
        input_message = create_input_message(char_a, char_b)
        print(input_message)


    return events_to_display

@app.route('/game', methods=['GET', 'POST'])
def play():
    """On get displays a list of remaining characters, on post displays a list of events"""
    form = NextEvent()
    if request.method == 'POST':
        # check if winner, if so render winner
        if len(characters) == 1:
            return render_template("winner.html", form=form, winner=characters[0].name)
        print ("helloooo")
        generate_event()
        return render_template("event.html", form=form, events=events)
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