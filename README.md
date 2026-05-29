## 🤖 AI-Chatbot
A fun and interactive AI chatbot built with Streamlit, LangChain, and Groq's LLaMA 3.3 70B model. Switch between three unique personality modes — Angry, Funny, or Sad — and have a conversation with an AI that matches your vibe!

✨ Features

🧠 Powered by LLaMA 3.3 70B via Groq's ultra-fast inference API
🎭 Three Personality Modes:

😡 Angry Mode — Aggressive and impatient responses
😂 Funny Mode — Humorous replies packed with jokes
😢 Sad Mode — Emotional and melancholic tone


💬 Persistent Chat History within each session
🔄 Auto-reset when switching modes — fresh context every time
⚡ Real-time responses with a clean Streamlit chat UI


## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit] | Web UI framework |
| [LangChain] | LLM orchestration |
| [Groq] | LLM inference (LLaMA 3.3 70B) |
| [python-dotenv] | Environment variable management |

## ⚙️ How It Works

The user selects a personality mode from the sidebar.
A system prompt sets the AI's persona for the session.
User messages are appended to the chat history as HumanMessage objects.
The full conversation history is sent to Groq's LLaMA 3.3 70B model via LangChain.
The AI response is displayed and stored as an AIMessage.
Switching modes resets the chat history with a new system prompt.




