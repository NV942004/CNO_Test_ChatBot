class ResponseGenerator:
    def __init__(self, products):
        self.products = products

    def generate_response(self, user_input):
        # Here you would implement logic to analyze user_input
        # and recommend products based on the input.
        # For now, we'll return a placeholder response.
        return "Thank you for your inquiry! Based on your input, I recommend the following products: " + ", ".join(self.products.keys())

    def format_response(self, recommendations):
        # Format the recommendations into a user-friendly string
        return "Here are the products I recommend for you: " + ", ".join(recommendations)