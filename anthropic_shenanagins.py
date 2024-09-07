import os
from dotenv import load_dotenv
import anthropic
import json
import logging
import time


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class AnthropicClient:
    # Constants
    MODEL_NAME = "claude-3-haiku-20240307"
    MAX_TOKENS = 1000
    TEMPERATURE = 0

    def __init__(self):
        # Create client and authenticate
        load_dotenv()
        self.api_key = os.getenv('API_KEY') # get api_key from .env
        self.client = anthropic.Anthropic(api_key= self.api_key) # create client

        # Load system prompt from file
        with open('system_prompt.txt', 'r') as file:
            self.system_prompt = file.read()

    @staticmethod
    def format_input_text(char_a, char_b, context):
        """Takes character objects, formats and returns their attributes as a string"""
        # Formats char_a's information
        formatted_input = (f"'Input:'"
                        f"'Focus: [{char_a.name}, {char_a.status}, {char_a.last_event}, {char_a.items}]")

        # Format char_b's information, if it has any
        if char_b is not None:
            formatted_input += f"\n'Scene: [{char_b.name}, {char_b.status}, {char_b.last_event}, {char_b.items}]'"

        formatted_input += f'Overall_Context: "{context}"'

        return formatted_input


    def send_message(self, input_message):
        """Sends input to language model and returns the output as a json"""
        logger.info(f"Sending message to AI: {input_message}")
        response =  self.client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=self.MAX_TOKENS,
            temperature=self.TEMPERATURE,
            system=self.system_prompt,
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

        logger.info(f"Received response from AI: {response.content[0].text}")
        time.sleep(5)
        return response

    @staticmethod
    def response_to_json(response):
        """Returns AI's response object into json format"""
        processed_response = response.content[0].text
        return json.loads(processed_response)





