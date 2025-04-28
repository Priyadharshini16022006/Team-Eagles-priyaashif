class Chatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hello! How can I assist you today?",
            "pricing": "Our pricing depends on the plan you choose. Can you specify which service you need?",
            "support": "Our support team is available 24/7. How can I help you?",
            "bye": "Goodbye! Have a great day!",
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        return self.responses.get(user_input, "I'm sorry, I didn't understand that. Can you rephrase?")

# Example conversation loop
chatbot = Chatbot()
while True:
    user_query = input("You: ")
    if user_query.lower() == "exit":
        print("Chatbot: Thank you! Goodbye!")
        break
    print(f"Chatbot: {chatbot.get_response(user_query)}")
