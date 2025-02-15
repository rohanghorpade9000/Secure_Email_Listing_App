import imapclient
import email
from email.header import decode_header
import os
from backend.app.api.db.mongodb import users_collection  # Import database connection

# Directory to save attachments
ATTACHMENTS_DIR = "backend/attachments"

async def fetch_emails(user_email: str):
    try:
        # Fetch user credentials from the database
        user_data = await users_collection.find_one({"email": user_email})
        if not user_data or "password" not in user_data:
            return {"error": "Email credentials not found for the user"}

        EMAIL_PASSWORD = user_data["password"]  # Fetch stored password (app password)

        # Ensure attachment folder exists
        os.makedirs(ATTACHMENTS_DIR, exist_ok=True)

        # Connect to email server
        client = imapclient.IMAPClient("imap.gmail.com", ssl=True)
        client.login(user_email, EMAIL_PASSWORD)
        client.select_folder("INBOX")

        # Fetch latest 10 emails
        messages = client.search("ALL")[-10:]
        email_list = []

        for msg_id in messages:
            raw_message = client.fetch([msg_id], ["RFC822"])[msg_id][b"RFC822"]
            msg = email.message_from_bytes(raw_message)

            # Decode email fields
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")

            sender = msg.get("From")
            date = msg.get("Date")

            attachments = []
            for part in msg.walk():
                if part.get_content_disposition() == "attachment":
                    filename = part.get_filename()
                    if filename:
                        filepath = os.path.join(ATTACHMENTS_DIR, filename)
                        with open(filepath, "wb") as f:
                            f.write(part.get_payload(decode=True))
                        attachments.append(filename)

            email_list.append({
                "id": msg_id,
                "subject": subject,
                "sender": sender,
                "timestamp": date,
                "attachments": attachments  # List of saved attachments
            })

        client.logout()
        return email_list

    except Exception as e:
        return {"error": str(e)}
