from modules.chat import chat_with_nyx, welcome_nyx
from modules.memory import save_chat_log, load_chat_log

def main():
    welcome_nyx()

    print("🔮 Nyx AI: Your personal AI assistant is now active!\n")
    
    chat_history = load_chat_log()  # Load previous chats
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Nyx: Goodbye! Catch you later. 🖤")
            save_chat_log(chat_history)  # Save chat before exiting
            break
        
        response, chat_history = chat_with_nyx(user_input, chat_history)
        print(f"Nyx: {response}")

if __name__ == "__main__":
    main()
