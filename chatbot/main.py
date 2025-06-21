from chatbot.nlp_engine import get_answer

def run_chatbot():
    print("🎓 Welcome to the Student Support Chatbot!")
    print("📚 Student Support Chatbot (type 'exit' to quit)")
    while True:
        query = input("You: ")
        if query.lower() == 'exit':
            break
        response = get_answer(query)
        print("Bot:", response)

if __name__ == "__main__":
    run_chatbot()
