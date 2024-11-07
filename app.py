import streamlit as st
from utils import load_model, generate_response

# Load the model once
model = load_model()

# Initialize chat history in Streamlit session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Title and description
st.title("Chatbot - Your Empathetic Companion")
st.write("I'm here to chat with you. Type 'bye' to end the conversation.")

# Display chat history
for message in st.session_state["chat_history"]:
    if message["role"] == "user":
        st.markdown(f"<div style='text-align: right; color: blue; background-color: #e0f7fa; padding: 10px; border-radius: 10px; max-width: 70%; margin: 5px auto;'>You: {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; color: black; background-color: #f1f0f0; padding: 10px; border-radius: 10px; max-width: 70%; margin: 5px auto;'>Chatbot: {message['content']}</div>", unsafe_allow_html=True)

# User input
user_input = st.text_input("Type your message here...", key="input")

# Process user input and generate response if input is not empty
if st.button("Send") and user_input:
    # Add user message to chat history
    st.session_state["chat_history"].append({"role": "user", "content": user_input})

    # Generate response
    bot_response = generate_response(model, user_input)
    st.session_state["chat_history"].append({"role": "bot", "content": bot_response})

    # Clear the input box by resetting the key value
    st.session_state["input"] = ""
