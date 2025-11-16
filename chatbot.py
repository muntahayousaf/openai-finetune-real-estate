import streamlit as st
from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"  # <-- paste your real key here

client = OpenAI()

MODEL_NAME = "ft:gpt-4o-mini-2024-07-18:level-up::CcWKkPYl" 

st.set_page_config(page_title="Fine-Tuned Chatbot")
st.title("🤖 My Fine-Tuned Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=st.session_state.messages,
    )

    bot_reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.write(bot_reply)


