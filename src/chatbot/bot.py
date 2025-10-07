from src.data.intents import intents
from src.data.products import brands_products
from src.chatbot.intent_classifier import IntentClassifier
from src.chatbot.response_generator import ResponseGenerator
import random

class ChatBot:
    def __init__(self):
        self.intent_classifier = IntentClassifier(intents)
        self.response_generator = ResponseGenerator(brands_products)

    def get_response(self, user_input):
        # Classify the intent
        intent = self.classify_user_intent(user_input)
        
        if intent == "greeting":
            return random.choice(intents["greeting"]["responses"])
        elif intent == "insurance_inquiry" or intent == "product_recommendation":
            return "I recommend exploring our CNO Financial Group products including Life Insurance, Health Insurance, and Annuities."
        elif intent == "goodbye":
            return random.choice(intents["goodbye"]["responses"])
        else:
            return "I'm sorry, I didn't understand that. Could you please rephrase your question?"

    def classify_user_intent(self, user_input):
        user_input_lower = user_input.lower()
        
        for intent_name, intent_data in intents.items():
            for example in intent_data["examples"]:
                if any(word in user_input_lower for word in example.lower().split()):
                    return intent_name
        
        return "unknown"

    def start_conversation(self):
        print("Welcome to the CNO Financial Group Insurance Chatbot!")
        print("Type 'exit' or 'quit' to end the conversation.")
        print()
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Chatbot: Thank you for chatting! Goodbye!")
                break
            
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")
            print()