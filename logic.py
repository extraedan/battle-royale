from anthropic_shenanagins import create_input_message, send_message, update_characters
from characters import Character
import random

characters = [None, None, None, None]



def generate_event():
    events_to_display = []
    character_pool = [character for character in characters if character.death == False]

    while character_pool:
        char_a = character_pool.pop(0)
        char_b = None

        if random.choice([True, False]) and len(character_pool) > 0:
            char_b = random.choice(character_pool)
            character_pool.remove(char_b)

        input_message = create_input_message(char_a, char_b)
        output = send_message(input_message)
        event = output["event"]
        events_to_display.append(event)

        update_characters(char_a, char_b, output)

    return events_to_display

def create_edit_character(form):
    """Processes form input to create a new character or edit an existing one based on the slot number."""

    index = int(form.slot.data) # get the character slot from the form
    name = form.name.data # get the character name from the form

    # Creating new characters
    if characters[index] is None: # if no character is in that slot
        characters[index] = Character(name, index) # make a new character, passing in name and slot ID

    # Edit character name if it already exists
    else:
        characters[index].name = name

def get_characters():
    return characters
g
