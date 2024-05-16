import random
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get your Twilio account SID, Auth Token, and phone numbers from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')
to_number = os.getenv('TO_NUMBER')

# Create a client to interact with the Twilio API
client = Client(account_sid, auth_token)

# List of random messages
messages = [
    "Hello! How's your day going?",
    "Just checking in on you.",
    "Hope you're having a great day!",
    "Don't forget to smile!",
    "Here's a random message for you!"
]

# Function to send a random message
def send_random_message():
    # Choose a random message from the list
    message = random.choice(messages)
    
    # Send the message using Twilio
    message = client.messages.create(
        body=message,
        from_=twilio_number,
        to=to_number
    )
    
    print(f"Sent message: {message.body}")

# Call the function to send a message
send_random_message()
