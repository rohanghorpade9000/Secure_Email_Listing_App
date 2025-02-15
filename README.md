# Secure_Email_Listing_App

📌 Project Overview

This project is a Secure Email Document Listing Application built using FastAPI (backend) and Streamlit (frontend). It allows users to log in, fetch emails, view attachments, and download files securely.

✅ Key Features:

User Authentication (JWT-based) – Secure login & signup.

Fetch Emails – Retrieve user-specific emails from IMAP.

Download Attachments – Securely download attached documents.

Streamlit UI – Simple and interactive frontend.

MongoDB via Docker – Stores user credentials securely.

🛠️ Tech Stack

Backend: FastAPI

Frontend: Streamlit

Database: MongoDB (running via Docker)

Email Fetching: IMAP

Authentication: JWT

🚀 Setup & Installation

1️⃣ Clone the Repository

git clone https://github.com/rohanghorpade9000/secure-email-app.git
cd secure-email-app

2️⃣ Run MongoDB via Docker

docker run -d --name Easeworkai_mongo -p 27019:27017 -e MONGO_INITDB_ROOT_USERNAME=easeworkai_admin -e MONGO_INITDB_ROOT_PASSWORD=easeworkai_password -v easeworkai_mongo_data:/data/db mongo

3️⃣ Set Up FastAPI Backend (Locally)

cd backend
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
uvicorn app.api.main:app --reload

4️⃣ Run Streamlit Frontend

cd frontend
pip install -r requirements.txt
streamlit run main.py

🔗 API Endpoints & Usage

1️⃣ Authentication

🔹 Signup

Endpoint: POST /auth/signup

{
    "email": "user@example.com",
    "password": "email_password"
}

Response:

{
    "message": "User registered successfully"
}

🔹 Login

Endpoint: POST /auth/login

{
    "email": "user@example.com",
    "password": "email_password"
}

Response:

{
    "access_token": "jwt_token_here",
    "token_type": "bearer"
}

2️⃣ Fetch & Download Emails

🔹 Fetch Emails (JWT Required)

Endpoint: GET /emails
Headers: Authorization: Bearer <jwt_token>
Response:

{
    "emails": [
        {
            "id": 123,
            "subject": "Invoice Attached",
            "sender": "billing@company.com",
            "timestamp": "2025-02-14T10:00:00Z",
            "attachments": ["invoice.pdf"]
        }
    ]
}

🔹 Download Attachment (JWT Required)

Endpoint: GET /emails/{filename}/download
Headers: Authorization: Bearer <jwt_token>
Response: Downloads the file.

🔗 Using the Application via Streamlit

1️⃣ Authentication

🔹 Signup

Open the Streamlit frontend (streamlit run main.py).

Navigate to the Signup Page.

Enter your email and password, then click Sign Up.

If successful, you will see a success message and can proceed to log in.

🔹 Login

Open the Streamlit frontend (streamlit run main.py).

Navigate to the Login Page.

Enter your email and password, then click Login.

If successful, you will be redirected to the dashboard.

📌 Future Improvements

🔒 Enhance Security – Encrypt stored passwords in MongoDB.

🔄 Auto-refresh emails – Implement real-time email fetching.

🎨 Improve UI – Make Streamlit more visually appealing.

🚀 Deploy Online – Host the app for public access.
