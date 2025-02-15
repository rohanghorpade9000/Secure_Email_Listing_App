import streamlit as st
from pages.login import show_login
from pages.signup import show_signup
from pages.dashboard import show_dashboard

# Navigation state
if "page" not in st.session_state:
    st.session_state["page"] = "login"

# Page Navigation Logic
if "jwt_token" in st.session_state:
    show_dashboard()
else:
    if st.session_state["page"] == "login":
        show_login()
        if st.button("Create an Account"):
            st.session_state["page"] = "signup"
            st.rerun()
    else:
        show_signup()
        if st.button("Already have an account? Login"):
            st.session_state["page"] = "login"
            st.rerun()
