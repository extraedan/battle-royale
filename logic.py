from anthropic_shenanagins import create_input_message, send_message, update_characters
from characters import Character
import random

characters = [None, None, None, None]

def generate_event():
    """Generate and return a list of events to display for the round"""
    events_to_display = []

    # create a list of living characters to choose from
    character_pool = [character for character in characters if character.death == False]

    while character_pool:
        char_a, char_b = select_event_characters(character_pool) # select one or two characters to be in an event

        # AI STUFF
        input_message = create_input_message(char_a, char_b) # create the input message
        output = send_message(input_message) # pass the input message and get output
        events_to_display.append(output["event"]) # add event text to list

        update_characters(char_a, char_b, output) # update attributes of characters

    # return list of events to display strings to route
    return events_to_display

def select_event_characters(character_pool):
    char_a = character_pool.pop(0)  # choosing first character and removing it from pool
    char_b = None  # by default char_b is None

    if random.choice([True, False]) and len(character_pool) > 0:  # 50% chance of char_b
        char_b = random.choice(character_pool)  # choose char_b randomly
        character_pool.remove(char_b)  # remove char_b from pool

    return char_a, char_b

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

