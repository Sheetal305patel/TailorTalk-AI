import streamlit as st
import requests

st.set_page_config(
    page_title="TailorTalk AI",
    page_icon="📁"
)

st.title("📁 TailorTalk AI Assistant")

st.caption("Search your Google Drive files using AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask about your files...")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Searching files..."):

            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={
                    "message": prompt
                }
            )

            data = response.json()

            st.markdown(data["response"])

    st.session_state.messages.append({
        "role": "assistant",
        "content": data["response"]
    })