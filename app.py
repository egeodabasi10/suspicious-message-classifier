import json
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Suspicious Message Classifier",
    page_icon="🔍",
    layout="centered"
)

st.title("Suspicious Message Classifier")

st.write(
    "An interactive prototype exploring how AI recommendations "
    "influence human decisions when identifying suspicious messages."
)

# Load predefined messages
messages_path = Path(__file__).parent / "messages.json"

with messages_path.open("r", encoding="utf-8") as file:
    messages = json.load(file)

st.subheader("Step 1: Review a Message")

selected_message = st.selectbox(
    "Choose a message to review:",
    messages,
    format_func=lambda message: message["title"]
)

st.markdown(f"**From:** {selected_message['sender']}")
st.markdown(f"**Subject:** {selected_message['title']}")

st.text_area(
    "Message content",
    value=selected_message["content"],
    height=150,
    disabled=True
)

st.subheader("Step 2: Make Your Initial Judgement")

initial_judgement = st.radio(
    "Do you think this message is safe or suspicious?",
    ["Safe", "Suspicious"],
    index=None
)

if st.button("Submit Initial Judgement"):
    if initial_judgement is None:
        st.warning("Please select a classification before continuing.")
    else:
        st.success(f"Your initial judgement: {initial_judgement}")
        st.info(
            "Your judgement has been recorded. "
            "AI recommendations will be introduced in the next stage."
        )
