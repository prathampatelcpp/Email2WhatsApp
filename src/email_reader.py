import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Read-only Gmail permission
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.json")
TOKEN_FILE = os.path.join(BASE_DIR, "token.pickle")


def authenticate_gmail():

    creds = None

    # Check whether a token already exists
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "rb") as token:
            creds = pickle.load(token)

    # Refresh or request authorization
    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save authentication token
        with open(TOKEN_FILE, "wb") as token:
            pickle.dump(creds, token)

    # Build Gmail service
    service = build("gmail", "v1", credentials=creds)

    return service



def get_latest_emails(service):
    # Fetch the latest 5 email message IDs
    results = service.users().messages().list(
        userId="me",
        maxResults=5
    ).execute()

    messages = results.get("messages", [])
    email_list = []

    # Fetch details of each email
    for message in messages:
        email = service.users().messages().get(
            userId="me",
            id=message["id"],
            format="metadata",
            metadataHeaders=["From", "Subject", "Date"]
        ).execute()

        # Extract email headers
        headers = email.get("payload", {}).get("headers", [])

        details = {
            header["name"].lower(): header["value"]
            for header in headers
        }

        # Store email information
        email_data = {
            "id": email["id"],
            "sender": details.get("from", "Unknown"),
            "subject": details.get("subject", "No subject"),
            "date": details.get("date", "Unknown"),
            "snippet": email.get("snippet", "")
        }

        email_list.append(email_data)

    return email_list


if __name__ == "__main__":

    gmail_service = authenticate_gmail()

    print("Gmail connected successfully!")

    get_latest_emails(gmail_service)
