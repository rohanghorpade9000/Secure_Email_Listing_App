import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"


def show_dashboard():
    st.title("📬 Email Dashboard")

    # Check if the user is logged in
    if "jwt_token" not in st.session_state:
        st.warning("⚠️ You are not logged in. Please log in first.")
        st.stop()

    # Fetch emails from backend
    headers = {"Authorization": f"Bearer {st.session_state['jwt_token']}"}
    response = requests.get(f"{API_URL}/emails", headers=headers)

    if response.status_code == 200:
        emails = response.json().get("emails", [])
        if not emails:
            st.info("📭 No emails found.")
        else:
            for email in emails:
                with st.expander(f"📩 {email['subject']} (From: {email['sender']})"):
                    st.write(f"📅 **Date:** {email['timestamp']}")
                    if email.get("attachments"):
                        st.write("📎 **Attachments:**")
                        for attachment in email["attachments"]:
                            file_url = f"{API_URL}/emails/{attachment}/download"

                            # ✅ Fetch the file as binary data instead of using URL
                            file_response = requests.get(file_url, headers=headers)

                            if file_response.status_code == 200:
                                file_bytes = file_response.content  # ✅ Get binary content
                                st.download_button(
                                    label=f"Download {attachment}",
                                    data=file_bytes,
                                    file_name=attachment,
                                    mime="application/octet-stream",
                                    key=f"download_{email['id']}_{attachment}"
                                )
                            else:
                                st.error(f"❌ Failed to fetch {attachment}")
    else:
        st.error("❌ Failed to fetch emails. Please try again later.")

    # Logout Button
    if st.button("Logout"):
        del st.session_state["jwt_token"]
        st.success("✅ Logged out successfully!")
        st.rerun()  # Refresh UI to go back to login
