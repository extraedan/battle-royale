from flask import render_template, request, redirect, url_for, flash
from forms import InputCharacter, NextEvent, CharacterAmount
from logic import *

def init_routes(app):


    @app.route('/game', methods=['GET', 'POST'])
    def play():
        round_number = increase_round_number()
        form = NextEvent() # Create next event form
        characters = get_characters() # Fetch the character list

        if request.method == 'POST':
            # TODO: replace the check for winner with a function in game logic
            if check_for_winner():
                winner = get_living_characters()[0]
                return render_template("winner.html", form=form, winner=winner)

            displayed_events = generate_event()
            return render_template("event.html", form=form, events=displayed_events, game=game)

        # Render the form page for a GET request
        return render_template("game.html", game=game, form=form)

    @app.route('/')
    def home():
        reset_game()
        return render_template("index.html")

    @app.route('/reset')
    def reset():
        reset_game()
        return redirect(url_for('choose_characters'))

    @app.route('/count', methods=['GET', 'POST'])
    def character_amount():
        form = CharacterAmount()
        if request.method == 'POST':
            if form.validate_on_submit():
                game.character_amount = form.amount.data
                create_character_slots(game.character_amount)
                return redirect(url_for('choose_characters'))  # Redirect to choose_characters

        return render_template("character_amount.html", form=form)

    @app.route('/create', methods=['GET', 'POST'])
    def choose_characters():
        """Handle character creation and editing."""
        forms = [InputCharacter() for _ in range(game.character_amount)]  # Create the forms
        messages = []

        # Handle form submission
        if request.method == 'POST':
            for form in forms:
                if form.validate_on_submit():
                    name = form.name.data  # get the character name from the form
                    index = int(form.slot.data)  # get the character slot from the form
                    if check_if_duplicate(name,index):
                        messages.append(('error', f'Error: Character name "{name}" already exists.'))
                    else:
                        create_edit_character(name,index)  # Create or edit character that was submitted
                        messages.append(('success', f'Character "{name}" successfully created/edited.'))

            for category, message in set(messages):
                flash(message, category)

            return redirect(url_for('choose_characters'))  # Redirect after processing all forms

        # Render the form page for a GET request
        return render_template("choose_characters.html", forms=forms, game=game)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404


    return app