import unittest
from src.chatbot.bot import ChatBot

class TestChatBot(unittest.TestCase):

    def setUp(self):
        self.chatbot = ChatBot()

    def test_greeting(self):
        response = self.chatbot.get_response("Hello")
        self.assertIn("Hi", response)

    def test_insurance_recommendation(self):
        response = self.chatbot.get_response("What insurance do you recommend?")
        self.assertIn("I recommend", response)

    def test_unknown_intent(self):
        response = self.chatbot.get_response("Blah blah")
        self.assertIn("I'm sorry", response)

if __name__ == '__main__':
    unittest.main()