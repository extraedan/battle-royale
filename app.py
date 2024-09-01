from flask import Flask, render_template, request, redirect, url_for
from forms import InputCharacter, NextEvent
from flask_bootstrap import Bootstrap
from characters import Character
from events import events
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
    """Returns a list of randomly generated event strings"""
    current_events = []
    for character in characters:
        # 50% chance something happens to the character
        if random.choice([True, False]):
            char_a = character.name

            # chooses random event object
            event = random.choice(events)
            print(event)
            print(event.text)
            print(event.char_count)

            # if single event
            if event.char_count == 1:
                # reformats the text
                event = f"{event.text}".format(char_a=char_a)
                current_events.append(event)

            # if double event
            elif event.char_count == 2:
                # makes sure character b and character a are not the same
                chars_pool = [char for char in characters if char.name != char_a]
                char_b = random.choice(chars_pool).name
                event = f"{event.text}".format(char_a=char_a, char_b=char_b)
                current_events.append(event)
    return current_events

@app.route('/game', methods=['GET', 'POST'])
def play():
    """On get displays a list of remaining characters, on post displays a list of events"""
    if request.method == 'POST':
        form = NextEvent()
        events = generate_event()
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