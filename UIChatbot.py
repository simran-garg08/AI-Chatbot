import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

# Initialize model
model = ChatGroq(model="llama-3.3-70b-versatile")

# Streamlit UI
st.set_page_config(page_title="AI ChatBot", page_icon="🤖")

st.title("🤖 AI ChatBot")

# Sidebar for mode selection
st.sidebar.title("Choose AI Mode")

mode_option = st.sidebar.radio(
    "Select Mode",
    ("Angry Mode", "Funny Mode", "Sad Mode")
)

# Define system prompt
if mode_option == "Angry Mode":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif mode_option == "Funny Mode":
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif mode_option == "Sad Mode":
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# Reset chat when mode changes
if "current_mode" not in st.session_state:
    st.session_state.current_mode = mode_option

if st.session_state.current_mode != mode_option:
    st.session_state.current_mode = mode_option
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# Display previous messages
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# User input
prompt = st.chat_input("Type your message...")

if prompt:
    # Show user message
    with st.chat_message("user"):
        st.write(prompt)

    # Store user message
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Get AI response
    response = model.invoke(st.session_state.messages)

    # Store AI response
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    # Show AI response
    with st.chat_message("assistant"):
        st.write(response.content)