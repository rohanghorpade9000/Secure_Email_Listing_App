import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000"

def show_signup():
    st.title("📝 Create an Account")

    # Input fields for signup
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type="password")

    if st.button("Sign Up"):
        if not email or not password:
            st.error("⚠️ Please enter both email and password.")
        else:
            response = requests.post(f"{API_URL}/auth/signup", json={"email": email, "password": password})

            if response.status_code == 200:
                st.success("✅ Account created successfully! Please log in.")
                st.rerun()  # Refresh to switch to login
            else:
                st.error("❌ Email already registered or invalid data.")
