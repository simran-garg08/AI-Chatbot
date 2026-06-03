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




## Angry Mode - 
<img width="1919" height="981" alt="image" src="https://github.com/user-attachments/assets/8d0d61c4-9ea9-4981-a93f-98cd2083992a" />

## Funny Mode - 
<img width="1915" height="976" alt="image" src="https://github.com/user-attachments/assets/a681979d-f7ff-4fdc-a288-4fb2d357071d" />

## Sad Mode - 
<img width="1919" height="969" alt="image" src="https://github.com/user-attachments/assets/0dade72e-f40c-44e2-aeca-6d5105460055" />







