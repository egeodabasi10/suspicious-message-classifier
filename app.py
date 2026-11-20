
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

st.subheader("Message Analysis")

message = st.text_area(
    "Message to analyse",
    placeholder="Enter or paste a message here...",
    height=150
)

if st.button("Analyse Message"):
    if message.strip():
        st.info("Message received. AI analysis will be added later.")
    else:
        st.warning("Please enter a message first.")
