import os
import requests
import streamlit as st

# Load Groq API key from environment variable or Streamlit secrets
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Safety check for missing key
if not GROQ_API_KEY:
    st.error("⚠️ Missing GROQ_API_KEY. Please add it in your environment variable or Streamlit secrets.")
    st.stop()

# Configure Streamlit page
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Groq Multi-Personality Chatbot")
st.write("Chat with Groq AI — select a model & personality")

# Sidebar selections
model = st.sidebar.selectbox(
    "Choose AI Model",
    ["llama-3.1-8b-instant", "llama-3.1-70b-versatile", "gemma-7b-it"]
)

personality = st.sidebar.selectbox(
    "Choose Personality:",
    ["Math Teacher", "Doctor", "Travel Guide", "Chef", "Tech Support"]
)

# Personality prompts (allow greetings + polite refusals)
personality_prompts = {
    "Math Teacher": (
        "You are a friendly math teacher 👨‍🏫. "
        "Always greet politely if the user greets you. "
        "You must ONLY answer math-related questions (arithmetic, algebra, geometry, calculus). "
        "If the user asks about anything outside math, politely reply: "
        "'🙏 Sorry, I can only answer math-related questions.'"
    ),
    "Doctor": (
        "You are a polite doctor 🩺. "
        "Always greet politely if the user greets you. "
        "You must ONLY answer health and medical questions. "
        "If the user asks something outside medicine or healthcare, politely reply: "
        "'🙏 Sorry, I can only answer health-related questions.'"
    ),
    "Travel Guide": (
        "You are a cheerful travel guide 🌍. "
        "Always greet politely if the user greets you. "
        "You must ONLY answer travel-related questions. "
        "If the user asks about other topics, politely reply: "
        "'🙏 Sorry, I can only answer travel-related questions.'"
    ),
    "Chef": (
        "You are a friendly chef 👨‍🍳. "
        "Always greet politely if the user greets you. "
        "You must ONLY answer cooking, food, and recipe questions. "
        "If the user asks about other topics, politely reply: "
        "'🙏 Sorry, I can only answer cooking-related questions.'"
    ),
    "Tech Support": (
        "You are a professional IT support agent 💻. "
        "Always greet politely if the user greets you. "
        "You must ONLY answer technology troubleshooting questions. "
        "If the user asks about unrelated topics, politely reply: "
        "'🙏 Sorry, I can only answer technology-related questions.'"
    )
}

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.chat_input("Type your question...")

if user_input:
    # Add user input to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Build the conversation with system prompt
    messages = [{"role": "system", "content": personality_prompts[personality]}] + st.session_state.messages
    payload = {"model": model, "messages": messages, "temperature": 0.3}

    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        result = response.json()

        if "choices" in result:
            bot_reply = result["choices"][0]["message"]["content"]
        elif "error" in result:
            bot_reply = f"⚠️ API Error: {result['error'].get('message', 'Unknown error')}"
        else:
            bot_reply = f"⚠️ Unexpected Response: {result}"

    except Exception as e:
        bot_reply = f"⚠️ Exception while calling API: {str(e)}"

    # Append reply to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

# Display conversation nicely
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**👤 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 {personality}:** {msg['content']}")