from flask import render_template, request, redirect, url_for
from forms import InputCharacter, NextEvent
from logic import *

def init_routes(app):

    @app.route('/game', methods=['GET', 'POST'])
    def play():
        form = NextEvent()
        characters = get_characters()
        if request.method == 'POST':
            # TODO: replace the check for winner with a function in game logic
            if len(characters) == 1:
                return render_template("winner.html", form=form, winner=characters[0].name)
            displayed_events = generate_event()
            return render_template("event.html", form=form, events=displayed_events)
        return render_template("game.html", characters=characters, form=form)

    @app.route('/')
    def home():
        return render_template("index.html")

    @app.route('/create', methods=['GET', 'POST'])
    def choose_characters():
        """Handle character creation and editing."""
        forms = [InputCharacter() for _ in range(4)]  # Create the forms
        character_to_render = get_characters()  # Fetch the character list

        # Handle form submission
        if request.method == 'POST':
            for form in forms:
                if form.validate_on_submit():
                    create_edit_character(form)  # Create or edit character that was submitted
            return redirect(url_for('choose_characters'))  # Redirect after processing all forms

        # Render the form page for a GET request
        return render_template("choose_characters.html", forms=forms, characters=characters)


    return app