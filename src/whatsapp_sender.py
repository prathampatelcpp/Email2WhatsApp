import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load credentials from the project's .env file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Read Twilio credentials
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")
WHATSAPP_TO = os.getenv("TWILIO_WHATSAPP_TO")


def send_whatsapp_message(message_body):
    if not all([ACCOUNT_SID, AUTH_TOKEN, WHATSAPP_FROM, WHATSAPP_TO]):
        raise ValueError("Missing Twilio configuration in .env")

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        from_=WHATSAPP_FROM,
        to=WHATSAPP_TO,
        body=message_body
    )

    print("WhatsApp message sent successfully!")
    print("Message SID:", message.sid)


if __name__ == "__main__":
    send_whatsapp_message(
        "Hello! This is a test notification from my Email2WhatsApp Python project."
    )
