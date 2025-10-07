class Chatbot:
    def __init__(self, intent_classifier, response_generator):
        self.intent_classifier = intent_classifier
        self.response_generator = response_generator

    def start_conversation(self):
        print("Welcome to the CNO Financial Group Insurance Chatbot!")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Chatbot: Thank you for chatting! Goodbye!")
                break
            
            intent = self.intent_classifier.classify_intent(user_input)
            recommended_products = self.intent_classifier.get_recommended_products(intent)
            response = self.response_generator.generate_response(intent, recommended_products)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    from intent_classifier import IntentClassifier
    from response_generator import ResponseGenerator

    intent_classifier = IntentClassifier()
    response_generator = ResponseGenerator()
    chatbot = Chatbot(intent_classifier, response_generator)
    chatbot.start_conversation()