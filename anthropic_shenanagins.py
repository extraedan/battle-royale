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
                 'Include the scene character if provided. Provide only the output, in json format'
                 'Input: Focus: [Name, Health, LastEvent, Items] Scene: [Name, Health, LastEvent, Items]'
                 'Output:{ "event": "Event description", "updates":{ '
                 '"CharacterName": {"Health": int, "LastEvent": "string",'
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
        """Sends input to language model and returns the output object"""
        return client.messages.create(
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

def process_output(output):
    """Returns event message and updates attributes of character objects"""
    # extract text from output response
    print(output)
    output_data = json.loads(output)
    return output_data["event"]
# extract the text from the response
# claude_output = send_message().content[0].text
# event_data = json.loads(claude_output)
# print(event_data)
# print(event_data["event"])
# print(f"{char_a}'s health: {event_data['updates'][char_a]['Health']}")
# print(f"{char_b}'s health: {event_data['updates'][char_b]['Health']}")
# print(f"{char_a}'s last event: {event_data['updates'][char_a]['LastEvent']}")
# print(f"{char_b}'s last event: {event_data['updates'][char_b]['LastEvent']}")