import os
from dotenv import load_dotenv
import anthropic
import json

# load environment variables from .env file
load_dotenv()

# access the API key
api_key = os.getenv('API_KEY')

#// TODO: Find out how to disable context (these are individual messages that relay simple context so don't need them)

# create client
client = anthropic.Anthropic(api_key= api_key)


#// TODO: 50/50 shot it's a double, if it is a double then char_b no longer gets an event
system_prompt = ('generate a 1-2 sentence unique and creative Battle Royale event for the focus character, consider their status, last event, and items.'
                 'Include the scene character if provided. 50% chance of somebody dying. Provide only the output, in json format as shown below'
                 'Input: Focus: [Name, Status, LastEvent, Items] Scene: [Name, Status, LastEvent, Items]'
                 'Output:{ "event": "Event description", "updates":{ '
                 '"CharacterName": {"Status": "string", "LastEvent": "string",'
                 '"Items":[list], "Death": boolean}, ... } }')

# claude_input = ('Input:'
#          'Focus: [Luffy, 70, "found food", ["rope"]]'
#          'Scene: [Mable, 90, "got hit", ["slingshot"]]')

def create_input_message(char_a, char_b):
    """Takes character objects, formats and returns their attributes as a string"""
    # make initial message
    # if char B not None, add that too and append
    # return it
    claude_input = (f"'Input:'"
                    f"'Focus: [{char_a.name}, {char_a.status}, {char_a.last_event}, {char_a.items}]")
    if char_b != None:
        claude_input += f"\n'Scene: [{char_b.name}, {char_b.status}, {char_b.last_event}, {char_b.items}]'"
    return claude_input







# creating message to send
def send_message(input_message):
        """Sends input to language model and returns the output as a json"""
        data = client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=1000,
                    temperature=0,
                    system=system_prompt,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": input_message
                                }
                            ]
                        }
                    ]
                )

        process_output = data.content[0].text
        return json.loads(process_output)


def update_characters(char_a, char_b, output):
    """Updates character attributes with new values"""
    char_a.status = output["updates"][char_a.name]["Status"]
    char_a.last_event = output["updates"][char_a.name]["LastEvent"]
    char_a.items = output["updates"][char_a.name]["Items"]
    char_a.death = output["updates"][char_a.name]["Death"]

    if char_b is not None:
        char_b.status = output["updates"][char_b.name]["Status"]
        char_b.last_event = output["updates"][char_b.name]["LastEvent"]
        char_b.items = output["updates"][char_b.name]["Items"]
        char_b.death = output["updates"][char_b.name]["Death"]
