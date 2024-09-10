from anthropic_shenanagins import *
from characters import Character
import random

class GameState:
    def __init__(self):
        self.characters = []
        self.round_number = 0
        self.character_amount = 0
        self.context = "The battle royale has started"
        # Add other game state variables as needed

game = GameState()
ai_client = AnthropicClient()

def get_round_number():
    return game.round_number

def increase_round_number(num=1):
    game.round_number += 1
    return game.round_number

def reset_round_number():
    game.round_number = 0
    return game.round_number

def create_character_slots(num):
    """Fills the characters list with Nones, based on character amount requested"""
    for i in range(num):
        game.characters.append(None)

def generate_event():
    """Generate and return a list of events to display for the round"""
    events_to_display = []
    # create a list of living characters to choose from
    character_pool = [character for character in game.characters if character.death == False]

    # going through each character in the pool
    while character_pool:
        char_a, char_b = select_event_characters(character_pool) # select one or two characters to be in an event

        # Making API request
        input_text = ai_client.format_input_text(char_a, char_b, game.context) # format input message
        print(input_text)
        response = ai_client.send_message(input_text) # send message and receive output
        response_json = ai_client.response_to_json(response) # convert to json
        print(response_json)

        # Processing data
        update_character_attributes(char_a, char_b, response_json) # update attributes of characters
        update_context(response_json) # updates overall context
        events_to_display.append(response_json["event"]) # add event texts to list of events

    # return list of events to display strings to route
    return events_to_display

def select_event_characters(character_pool):
    char_a = character_pool.pop(0)  # choosing first character and removing it from pool
    char_b = None  # by default char_b is None

    if random.choice([True, False]) and len(character_pool) > 0:  # 50% chance of char_b
        char_b = random.choice(character_pool)  # choose char_b randomly
        character_pool.remove(char_b)  # remove char_b from pool

    return char_a, char_b


def update_character_attributes(char_a, char_b, output):
    """Updates character attributes with new values"""
    try:
        print(f"{char_a.name}: {char_a.death}")

        char_a.status = output["updates"][char_a.name]["Status"]
        char_a.last_event = output["updates"][char_a.name]["LastEvent"]
        char_a.items = output["updates"][char_a.name]["Items"]
        char_a.death = output["updates"][char_a.name]["Death"]
        print(f'From output: {output["updates"][char_a.name]["Death"]}')
        print(f"{char_a.name}: {char_a.death}")

        if char_b is not None:
            print(f"{char_b.name}: {char_b.death}")
            char_b.status = output["updates"][char_b.name]["Status"]
            char_b.last_event = output["updates"][char_b.name]["LastEvent"]
            char_b.items = output["updates"][char_b.name]["Items"]
            char_b.death = output["updates"][char_b.name]["Death"]
            print(f'From output: {output["updates"][char_b.name]["Death"]}')
            print(f"{char_b.name}: {char_b.death}")
    except KeyError as e:
        print(f"Key error in update_character_attributes: {e}")
    except Exception as e:
        print(f"Unexpected error in update_character_attributes: {e}")

def update_context(output):
    game.context = output["context"]

def create_edit_character(name,index,image=None):
    """Processes form input to create a new character or edit an existing one based on the slot number."""

    # Creating new characters
    if game.characters[index] is None: # if no character is in that slot
        game.characters[index] = Character(name, index) # make a new character, passing in name and slot ID

    # Edit character name if it already exists
    else:
        game.characters[index].name = name

    # Update image if there is one
    if image is not None:
        print(image)
        game.characters[index].image = image
        print(game.characters[index].image)

def check_if_duplicate(name, index):
    # Check if the name is already taken by another character
    existing_names = [c.name for c in game.characters if c is not None and c.id != index]
    if name in existing_names:
        return True


def get_characters():
    return game.characters

def check_for_winner():
    living_characters = get_living_characters()
    if len(living_characters) <= 1:
        return True

def get_living_characters():
    return [character for character in game.characters if character.death == False]

def reset_game():
    game.characters = [None, None, None, None]
    game.round_number = 0

