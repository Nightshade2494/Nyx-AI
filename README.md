# Nyx AI 🔮

Nyx AI is your personal AI assistant powered by Google’s Gemini 1.5 Pro!  
She’s playful, sarcastic, caring — basically your Gen Z AI bestie. 💬✨

---

## Features

- 🔮 **Chat with Nyx** — dynamic, friendly, and adaptable conversations  
- 🖥️ **Run shell commands** (`run ls`)  
- 🔎 **Google Search** directly (`search openai`)  
- 📅 **Event scheduler** placeholder (`schedule meeting at 5pm`)  
- 🎨 **Fancy welcome banners** and colored chat  
- 🛡️ **Environment variables** to protect private keys  

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/Nyx-AI.git
   cd Nyx-AI
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. **Install the requirements:**
   ```bash
   pip install -r requirements.txt
4. **Create a .env file in the project root:**
   ```bash
   touch .env
   ```
   **Inside .env, add:**
   ```int
   GEMINI_API_KEY=your-real-api-key-here
5. **Run Nyx:**
   ```bash
   python3 nyx_main.py

---

## Usage

When you launch Nyx, she will greet you with a flashy banner.
Just type and chat! 😎

**Example commands you can type:**
- Search weather tomorrow
- Schedule gym session
- Run ls
   
**Or just talk casually:**
- hey nyx what's up?
- i'm feeling sad today

**Nyx will vibe with you accordingly! 💖**

---

## Tech Stack

- Python 3.9+
- Google Generative AI (Gemini 1.5 Pro)
- rich (fancy terminal output)
- termcolor (colored text)
- python-dotenv (env var management)
- halo (loading spinners)
- pyfiglet (ASCII banners)

---

## Contributing

Feel free to fork and vibe up Nyx even more! 🎉
PRs welcome — check out the CONTRIBUTING.md for guidelines.

---

## License

MIT License

---

# ✅ Once you have all this ready:
Final push to GitHub:

```bash
git add .
git commit -m "Added README, moved API keys to env, prepared for open source 🌟"
git push
```
