def chatbot(user_input):
    user_input = user_input.lower().strip()
    
    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you today?"
    elif user_input in ["how are you", "how are you doing", "how do you do"]:
        return "I'm fine, thanks! How about you?"
    elif user_input in ["i'm good", "i am good", "fine", "good"]:
        return "That's great to hear!"
    elif user_input in ["what is your name", "who are you", "what are you"]:
        return "I'm a simple chatbot created to assist you!"
    elif user_input in ["what can you do", "help", "what do you do"]:
        return "I can chat with you! Try saying hello, asking how I am, or saying goodbye."
    elif user_input in ["tell me a joke", "joke"]:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif user_input in ["what time is it", "time"]:
        return "I don't have access to real-time data, but your device can tell you the time!"
    elif user_input in ["where are you from", "where do you live"]:
        return "I live inside your computer, running on Python!"
    elif user_input in ["thank you", "thanks", "thank you so much"]:
        return "You're welcome! Happy to help."
    elif user_input in ["bye", "goodbye", "see you", "exit", "quit"]:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure I understand. Could you try asking something else?"


print("Chatbot is running! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    response = chatbot(user_input)
    print(f"Bot: {response}")
    if user_input.lower().strip() in ["bye", "goodbye", "see you", "exit", "quit"]:
        break