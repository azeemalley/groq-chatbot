# 🤖 Groq Multi‑Personality Chatbot  

An AI-powered chatbot built using **Python**, **Streamlit**, and the **Groq Cloud API**.  

This app allows users to choose from different AI models, switch between multiple chatbot personalities, and ensures that each personality stays within its domain — politely refusing off-topic queries.  

---

🌍 **Live Demo**  
👉 [Click here to try the chatbot](https://groq-chatbot-g6pn576ry9erg9vlzvenae.streamlit.app/)  

📂 **Source Code**  
👉 [GitHub Repository](https://github.com/azeemalley/groq-chatbot)  

---

## ✨ Features  

- 🔹 **Multi‑Model Support** → Choose from `llama-3.1-8b-instant`, `llama-3.1-70b-versatile`, and `gemma-7b-it`  
- 🔹 **Personality Selector** → Switch between:  
  - 🧮 Math Teacher  
  - 🩺 Doctor  
  - 🌍 Travel Guide  
  - 👨‍🍳 Chef  
  - 💻 Tech Support  
- 🔹 **Polite Behavior** → Responds politely to greetings (*“hi”, “hello”*) and declines out-of-domain questions  
- 🔹 **Session Memory** → Maintains history during the chat session  
- 🔹 **Deployed Online** → Hosted on Streamlit Cloud for free, public access  

---

## 🛠️ Tech Stack  

- **Python**  
- **Streamlit** → Web App UI  
- **Groq API** → LLaMA & Gemma Large Language Models  
- **Streamlit Cloud** → Deployment  

---

## 💻 Run Locally  

```bash
# Clone the repo
git clone https://github.com/azeemalley/groq-chatbot.git
cd groq-chatbot

# Install dependencies
pip install -r requirements.txt

# Set your Groq API key
setx GROQ_API_KEY "your-groq-api-key"    # Windows
export GROQ_API_KEY="your-groq-api-key" # Mac/Linux

# Run the app
streamlit run app.py
