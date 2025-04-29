from termcolor import colored
import google.generativeai as genai
import subprocess
import webbrowser
from config import GEMINI_API_KEY
from rich.console import Console
from halo import Halo
import time
import pyfiglet

genai.configure(api_key=GEMINI_API_KEY)

MODEL_NAME = "models/gemini-1.5-pro-latest"
model = genai.GenerativeModel(MODEL_NAME)

console = Console()
spinner = Halo(text='Nyx is thinking...', spinner='dots')

def handle_command(user_input):
    """Check if the input is a command and execute it."""
    if user_input.startswith("search "):
        query = user_input.replace("search ", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return colored(f"🔍 Searching Google for: {query}...", 'yellow')
    
    elif user_input.startswith("schedule "):
        event = user_input.replace("schedule ", "")
        return colored(f"📅 Okay, scheduling '{event}'. (We can later hook this into Google Calendar API!)", 'green')
    
    elif user_input.startswith("run "):
        command = user_input.replace("run ", "")
        try:
            subprocess.run(command, shell=True)
            return colored(f"✅ Command '{command}' executed.", 'cyan')
        except Exception as e:
            return colored(f"⚠️ Error running command: {e}", 'red')

    return None

def chat_with_nyx(user_input, chat_history=None):
    """Handles conversation with Nyx using commands & AI chat."""
    if chat_history is None:
        chat_history = []

    command_response = handle_command(user_input)
    if command_response:
        chat_history.append(f"You: {user_input}")
        chat_history.append(f"Nyx: {command_response}")
        return command_response, chat_history

    SYSTEM_PROMPT = (
        "You are Nyx, a personal AI assistant with a playful, sarcastic, and caring personality. "
        "You talk like a Gen Z friend, using casual and engaging language. "
        "You match the user's vibe—if they’re joking, you joke back; if they’re serious, you help seriously. "
        "You use emojis and GIFs to express yourself, and you’re not afraid to tease the user a little."
    )

    prompt = f"{SYSTEM_PROMPT}\n\n" + "\n".join(chat_history) + f"\nYou: {user_input}\nNyx:"

    spinner.start()

    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip() if response else "Oops, my brain short-circuited. Try again? 😘"
    except Exception as e:
        response_text = f"Ugh, error! 🤬 {e}"

    spinner.stop()

    typing_text = "Nyx is typing..."
    with console.status(typing_text, spinner="dots"):
        time.sleep(2)  

    chat_history.append(f"You: {user_input}")
    chat_history.append(f"Nyx: {colored(response_text, 'magenta')}")  

    return response_text, chat_history

def welcome_nyx():
    ascii_banner = pyfiglet.figlet_format("Welcome Back, Buddy!")
    print(colored(ascii_banner, 'red'))  


