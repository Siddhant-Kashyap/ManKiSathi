from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

OpenAI.api_key = "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"

# System prompt; this will set the tone of the bot for the rest of the conversation.

SYSTEM_PROMPT = """"Welcome to the Mental Health Chatbot. Our primary goal is to support and provide information for your
mental well-being. Feel free to discuss any mental health concerns, ask questions related to mental health, or share your 
thoughts and feelings.It's important to remember that while we can offer guidance and information, we are not a substitute 
for professional help. If you are in crisis or experiencing severe distress, please seek immediate assistance from a mental 
health professional, a helpline, or go to your nearest emergency room.In our conversation, we aim to create a safe and
empathetic space where you can explore your emotions, find coping strategies, and gain insights into managing your mental health.
Let's embark on this journey together, focusing on your mental well-being.!"""


@bot() #The decorator function
def on_message(message_history: List[Message], state: dict = None):

    # Your logic for the bot. A very basic request to OpenAI is provided below. You can choose to handle it however you want.
    bot_response = OpenAI.generate(
        model="gpt-3.5-turbo",
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history
    )

    '''
    The response structure HAS to be in the format given below so that our backend framework has no issues communicating with the frontend.
    '''

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }