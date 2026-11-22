
from email_reader import authenticate_gmail, get_latest_emails
from whatsapp_sender import send_whatsapp_message
from database import (
    create_database,
    is_email_processed,
    mark_email_processed
)
ENABLE_WHATSAPP = False

def main():

    print("Starting Email2WhatsApp application...")

    # Step 1: Initialize database
    create_database()
    print("Database initialized successfully!")

    # Step 2: Authenticate Gmail
    gmail_service = authenticate_gmail()
    print("Gmail connected successfully!")

    # Step 3: Fetch latest emails
    emails = get_latest_emails(gmail_service)

    # Step 4: Process each email
    for email in emails:

        email_id = email["id"]

        # Check whether email was already processed
        if is_email_processed(email_id):
            print(f"Skipping duplicate email: {email['subject']}")
            continue

        print("\nNew email received!")
        print("From:", email["sender"])
        print("Subject:", email["subject"])

        # Step 5: Prepare WhatsApp notification
        message = (
            "New Email Received!\n\n"
            f"From: {email['sender']}\n"
            f"Subject: {email['subject']}\n"
            f"Date: {email['date']}\n\n"
            f"Preview: {email['snippet']}"
        )

        print("\nPrepared notification:")
        print(message)

        # Step 6: Send WhatsApp notification
        try:
            send_whatsapp_message(message)

            # Save email only after successful sending
            mark_email_processed(
                email_id,
                email["sender"],
                email["subject"]
            )

            print("Email processed successfully!")

        except Exception as error:
            print("WhatsApp notification failed!")
            print("Error:", error)
            print("Email will be retried during the next check.")

    print("\nEmail2WhatsApp execution completed!")


if __name__ == "__main__":
    main()
