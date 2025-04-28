import os

LOG_FILE = "logs/chat_logs.txt"

def save_chat_log(chat_history):
    """Saves chat history to a file."""
    with open(LOG_FILE, "w") as file:
        file.write("\n".join(chat_history))

def load_chat_log():
    """Loads chat history from a file if it exists."""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            return file.read().splitlines()
    return []
