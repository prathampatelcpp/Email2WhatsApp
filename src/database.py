
import sqlite3
import os

# Database location: project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "emails.db")


def create_database():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS processed_emails (
            email_id TEXT PRIMARY KEY,
            sender TEXT,
            subject TEXT,
            processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def is_email_processed(email_id):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT email_id FROM processed_emails WHERE email_id = ?",
        (email_id,)
    )

    result = cursor.fetchone()
    connection.close()

    return result is not None


def mark_email_processed(email_id, sender, subject):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO processed_emails
        (email_id, sender, subject)
        VALUES (?, ?, ?)
    """, (email_id, sender, subject))

    connection.commit()
    connection.close()
