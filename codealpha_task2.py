import datetime

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_date():
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")

def chatbot():
    print("🤖 Chatbot: Hello! I am your improved Python Chatbot. Type 'bye' to exit.")
    print("---------------------------------------------------------------")

    user_name = None

    while True:
        user = input("You: ").lower().strip()

        # Exit condition
        if user in ["bye", "exit", "quit", "goodbye"]:
            print("🤖 Chatbot: Goodbye! Have a wonderful day! 😊")
            break

        # Asking user's name
        elif user.startswith("my name is"):
            user_name = user.replace("my name is", "").strip().title()
            print(f"🤖 Chatbot: Nice to meet you, {user_name}! How can I help you today?")
        
        elif user == "what is my name":
            if user_name:
                print(f"🤖 Chatbot: Your name is {user_name}! 😄")
            else:
                print("🤖 Chatbot: You didn’t tell me your name yet!")
        
        # Greetings with multiple variations
        elif any(greet in user for greet in ["hi", "hello", "hey", "good morning", "good evening"]):
            print("🤖 Chatbot: Hello! How can I assist you today?")

        # Asking chatbot name
        elif "your name" in user:
            print("🤖 Chatbot: I am Python Chatbot v3.0!")

        # Asking well-being
        elif "how are you" in user:
            print("🤖 Chatbot: I'm doing great! Thanks for asking. 😊 How are you?")

        # Asking time
        elif "time" in user:
            print("⏰ Chatbot: The current time is", get_time())

        # Asking date
        elif "date" in user:
            print("📅 Chatbot: Today's date is", get_date())

        # Weather
        elif "weather" in user:
            print("🌦 Chatbot: I cannot check weather, but I hope it's a lovely day!")

        # Help menu
        elif user == "help":
            print("""
🤖 Chatbot Help Menu:
-------------------------
• greetings (hi, hello, hey)
• ask time        -> "time"
• ask date        -> "date"
• ask name        -> "your name"
• tell name       -> "my name is ..."
• ask joke        -> "joke"
• python info     -> "python"
• compliments     -> "love"
• college info    -> "college"
• food talk       -> "food"
• exit            -> "bye"
""")

        # Joke
        elif "joke" in user:
            print("😂 Chatbot: Why don’t robots get tired? Because they recharge automatically! ⚡")

        # Python
        elif "python" in user:
            print("🐍 Chatbot: Python is great for AI, data science, automation, websites, and more!")

        # Friendship
        elif "friend" in user:
            print("🤝 Chatbot: Of course! I am always here as your friend.")

        # Love keywords
        elif "love" in user:
            print("❤️ Chatbot: Love is the most beautiful feeling in the world!")

        # College
        elif "college" in user:
            print("🎓 Chatbot: Enjoy your college days, they are the best moments of life!")

        # Food
        elif "food" in user:
            print("🍕 Chatbot: I don't eat food, but I’d love to know your favourite dish!")

        # Extra smart keywords
        elif "thank" in user:
            print("😊 Chatbot: You're welcome!")

        elif "who created you" in user:
            print("🤖 Chatbot: I was created by a Python developer!")

        elif "what can you do" in user:
            print("🤖 Chatbot: I can talk, answer simple questions, tell jokes, and be your friend!")

        # Default fallback
        else:
            print("🤖 Chatbot: Hmm... I didn't understand that. Try typing 'help' to see commands.")

# Run the chatbot
chatbot()
