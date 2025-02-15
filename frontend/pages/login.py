import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000"

def show_login():  # ✅ Define this function
    st.title("🔑 Login to Your Email App")

    # Input fields for login
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type="password")

    # Login button
    if st.button("Login"):
        if not email or not password:
            st.error("⚠️ Please enter both email and password.")
        else:
            response = requests.post(f"{API_URL}/auth/login", json={"email": email, "password": password})

            if response.status_code == 200:
                token = response.json().get("access_token")
                st.session_state["jwt_token"] = token  # Store token in session
                st.success("✅ Logged in successfully!")
                st.rerun()  # Refresh UI to load dashboard
            else:
                st.error("❌ Invalid email or password")
