# intents.py

intents = {
    "greeting": {
        "examples": [
            "Hi",
            "Hello",
            "Good morning",
            "Good evening",
            "Hey"
        ],
        "responses": [
            "Hello! How can I assist you today?",
            "Hi there! What insurance product are you interested in?",
            "Greetings! What can I help you with?"
        ]
    },
    "insurance_inquiry": {
        "examples": [
            "Tell me about your insurance products",
            "What types of insurance do you offer?",
            "Can you recommend an insurance plan?",
            "I need information on insurance"
        ],
        "responses": [
            "We offer a variety of insurance products. What specific type are you interested in?",
            "Our insurance products include life, health, and auto insurance. Which one would you like to know more about?",
            "I can help you with information on our insurance plans. Please specify which type you're interested in."
        ]
    },
    "product_recommendation": {
        "examples": [
            "I need life insurance",
            "What about health insurance?",
            "Can you suggest an auto insurance plan?",
            "I'm looking for a good insurance policy"
        ],
        "responses": [
            "Based on your interest in life insurance, I recommend our comprehensive life coverage plan.",
            "For health insurance, our family health plan is a great option.",
            "If you're looking for auto insurance, our standard auto policy offers excellent coverage."
        ]
    },
    "goodbye": {
        "examples": [
            "Thank you",
            "Goodbye",
            "See you later",
            "Thanks for your help"
        ],
        "responses": [
            "You're welcome! If you have more questions, feel free to ask.",
            "Goodbye! Have a great day!",
            "Thank you for chatting with us. Take care!"
        ]
    }
}