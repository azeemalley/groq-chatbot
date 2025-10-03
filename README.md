🤖 Groq Multi‑Personality Chatbot
An AI-powered chatbot web app built with Streamlit and the Groq Cloud API.
This chatbot allows users to select from multiple Groq models and personalities, ensuring domain‑specific answers and polite refusals for off‑topic queries.

🌍 Live Demo: Try the Chatbot Here
📂 Source Code: GitHub Repository

✨ Features
🔹 Multiple Groq Models Supported

llama-3.1-8b-instant (fast, lightweight)
llama-3.1-70b-versatile (balanced, more capable)
gemma-7b-it (instruction-tuned model)
🔹 Personality Modes

🧮 Math Teacher → Only answers math questions
🩺 Doctor → Only health & medical queries
🌍 Travel Guide → Only travel tips/suggestions
👨‍🍳 Chef → Only cooking & recipe queries
💻 Tech Support → Only troubleshooting/IT help
🔹 Polite Behavior

Greets naturally (“Hi”, “Hello”)
Politely refuses irrelevant queries (“🙏 Sorry, I can only answer math-related questions.”)
🔹 Session Memory → Maintains conversation during an active session

🔹 Deployed on Streamlit Cloud → Free public hosting

🛠️ Tech Stack
Python 3.9+
Streamlit → Web UI framework
Groq Cloud API → LLaMA 3 & Gemma models
Hosting: Deployed free on Streamlit Cloud
## 💻 Run Locally

```bash
# Clone repo
git clone https://github.com/azeemalley/groq-chatbot.git
cd groq-chatbot

# Install dependencies
pip install -r requirements.txt

# Set your Groq API Key
setx GROQ_API_KEY "your-groq-api-key"    # Windows
export GROQ_API_KEY="your-groq-api-key" # Mac/Linux

# Run Streamlit app
streamlit run app.py
Then open 👉 http://localhost:8501
