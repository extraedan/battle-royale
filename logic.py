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
    """Creates a new character object or changes the name of an existing character object"""
    index = int(form.slot.data)
    name = form.name.data

    # if nobody in slot, create a new character object
    if characters[index] is None:
        characters[index] = Character(name)

    # if it already exists, just change the attribute
    else:
        characters[index].name = name
