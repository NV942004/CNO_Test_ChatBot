class IntentClassifier:
    def __init__(self, intents):
        self.intents = intents

    def classify_intent(self, user_input):
        for intent, keywords in self.intents.items():
            if any(keyword in user_input.lower() for keyword in keywords):
                return intent
        return None

    def get_coverage_categories(self, intent):
        coverage_mapping = {
            'life_insurance': ['term life', 'whole life', 'universal life'],
            'health_insurance': ['individual health', 'family health', 'critical illness'],
            'auto_insurance': ['liability', 'collision', 'comprehensive'],
            'home_insurance': ['homeowners', 'renters', 'landlord'],
        }
        return coverage_mapping.get(intent, [])