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



system_prompt = ('generate a 1-2 sentence Battle Royale event for the focus character, consider their status, last event, and items.'
                 'Optionally include the scene character. Provide only the output.'
                 'Input: Focus: [Name, Health, LastEvent, Items] Scene: [Name, Health, LastEvent, Items]'
                 'Output:{ "event": "Event description", "updates":{ '
                 '"CharacterName": {"Health": int, "LastEvent": "string",'
                 '"Items":[list], "Death": boolean}, ... } }')

claude_input = ('Input:'
         'Focus: [Luffy, 70, "found food", ["rope"]]'
         'Scene: [Mable, 90, "got hit", ["slingshot"]]')





# creating message to send
def create_message():
        return client.messages.create(
                    model="claude-3-5-sonnet-20240620",
                    max_tokens=1000,
                    temperature=0,
                    system=system_prompt,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": claude_input
                                }
                            ]
                        }
                    ]
                )

# extract the text from the response
char_a = "Luffy"
char_b = "Mable"
claude_output = create_message().content[0].text
event_data = json.loads(claude_output)
print(event_data)
print(event_data["event"])
print(f"{char_a}'s health: {event_data['updates'][char_a]['Health']}")
print(f"{char_b}'s health: {event_data['updates'][char_b]['Health']}")
print(f"{char_a}'s last event: {event_data['updates'][char_a]['LastEvent']}")
print(f"{char_b}'s last event: {event_data['updates'][char_b]['LastEvent']}")