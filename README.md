# Email2WhatsApp – Email Notification Automation

## Overview
Email2WhatsApp is a Python-based automation project designed to retrieve incoming emails from Gmail and convert important email information into WhatsApp notifications.

The objective is to reduce the need to repeatedly check the inbox by providing email updates through WhatsApp.

## Technologies Used
- Python
- Gmail API
- Google OAuth 2.0
- Twilio WhatsApp API
- SQLite (planned)
- python-dotenv

## Project Structure
```text
Email2WhatsApp/
├── src/
│   ├── main.py
│   ├── email_reader.py
│   └── whatsapp_sender.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Current Features
- Gmail API authentication using OAuth 2.0.
- Retrieve recent emails from Gmail.
- Extract sender, subject, date and email preview.
- Prepare WhatsApp notification messages.
- Secure configuration using environment variables.

## Setup Instructions

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   `pip install -r requirements.txt`

4. Configure Gmail API credentials in `credentials.json`.
5. Configure Twilio credentials in a `.env` file.
6. Run the application:

   `python src/main.py`

## Current Development Status

Gmail authentication and email retrieval are implemented.

WhatsApp delivery through Twilio is currently under development due to trial account restrictions.

## Future Improvements
- Complete WhatsApp notification integration.
- Implement SQLite-based duplicate email prevention.
- Add automatic email monitoring.
- Implement logging and exception handling.
- Improve notification formatting.
