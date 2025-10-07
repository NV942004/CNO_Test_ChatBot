"""
CNO Product Advisor - A Console-Based Insurance Recommendation Chatbot
======================================================================

This chatbot helps users discover suitable insurance or financial products 
offered by CNO Financial Group and its subsidiaries by asking targeted questions
and providing personalized recommendations.

Author: CNO Financial Group Development Team
Version: 1.0
"""

# Product database representing CNO Financial Group's brands and offerings
products = {
    "Bankers Life": {
        "categories": ["life", "retirement", "health"],
        "products": [
            "Term Life Insurance - Affordable temporary coverage for working families",
            "Whole Life Insurance - Permanent coverage with cash value growth", 
            "Medicare Supplement Insurance - Fill the gaps in Medicare coverage",
            "Fixed Indexed Annuity - Retirement income with growth potential",
            "Immediate Annuity - Start receiving income payments right away",
            "Long-Term Care Insurance - Coverage for extended care needs"
        ],
        "target_demographics": ["middle_income", "seniors", "working_families"]
    },
    "Colonial Penn": {
        "categories": ["life"],
        "products": [
            "Guaranteed Acceptance Whole Life - No medical exam required",
            "Simplified Issue Whole Life - Quick approval process",
            "Term Life Insurance - Budget-friendly temporary protection"
        ],
        "target_demographics": ["seniors", "simplified_underwriting"]
    },
    "Washington National": {
        "categories": ["supplemental", "health"],
        "products": [
            "Accident Insurance - Protection against unexpected injuries",
            "Cancer & Critical Illness Insurance - Financial support during serious illness",
            "Hospital Indemnity - Cash payments for hospital stays",
            "Supplemental Disability Coverage - Income protection when you can't work"
        ],
        "target_demographics": ["working_adults", "supplemental_coverage"]
    },
    "Optavise": {
        "categories": ["employee_benefits"],
        "products": [
            "Voluntary Benefits Packages - Comprehensive employee benefit solutions",
            "Benefits Education Tools - Help employees understand their options",
            "Advocacy Services - Support navigating insurance and benefits"
        ],
        "target_demographics": ["employers", "employee_groups"]
    },
    "myHealthPolicy.com": {
        "categories": ["health"],
        "products": [
            "Medicare Advantage - Comprehensive Medicare replacement plans",
            "Medicare Supplement - Additional coverage to work with Original Medicare",
            "Medicare Part D Prescription Drug Plans - Prescription drug coverage"
        ],
        "target_demographics": ["medicare_eligible", "seniors"]
    }
}

class CNOProductAdvisor:
    """
    Main chatbot class that handles user interaction and product recommendations
    """
    
    def __init__(self):
        """Initialize the chatbot with user response storage"""
        self.user_responses = {}
        self.recommended_brands = []
        
    def display_welcome(self):
        """Display welcome message and introduction"""
        print("=" * 60)
        print("🏦 Welcome to CNO Product Advisor! 👋")
        print("=" * 60)
        print()
        print("I'm here to help you discover the perfect insurance and financial")
        print("products from CNO Financial Group and our family of companies.")
        print()
        print("I'll ask you a few quick questions to understand your needs,")
        print("then recommend the best products and brands for your situation.")
        print()
        print("Let's get started! 🚀")
        print("-" * 60)
        print()
    
    def ask_age_range(self):
        """Ask user about their age range"""
        print("Question 1: What's your age range?")
        print("1. Under 40")
        print("2. 40-60") 
        print("3. 60+")
        
        while True:
            try:
                choice = input("\nEnter your choice (1-3): ").strip()
                if choice in ['1', '2', '3']:
                    age_mapping = {'1': 'under_40', '2': '40_60', '3': '60_plus'}
                    self.user_responses['age_range'] = age_mapping[choice]
                    print(f"✅ Got it! Age range: {['Under 40', '40-60', '60+'][int(choice)-1]}")
                    break
                else:
                    print("❌ Please enter 1, 2, or 3")
            except:
                print("❌ Please enter a valid number")
        print()
    
    def ask_employment_status(self):
        """Ask user about their employment status"""
        print("Question 2: What's your current employment status?")
        print("1. Employed")
        print("2. Self-employed")
        print("3. Retired")
        print("4. Nearing retirement")
        
        while True:
            try:
                choice = input("\nEnter your choice (1-4): ").strip()
                if choice in ['1', '2', '3', '4']:
                    status_mapping = {'1': 'employed', '2': 'self_employed', '3': 'retired', '4': 'nearing_retirement'}
                    self.user_responses['employment_status'] = status_mapping[choice]
                    print(f"✅ Employment status: {['Employed', 'Self-employed', 'Retired', 'Nearing retirement'][int(choice)-1]}")
                    break
                else:
                    print("❌ Please enter 1, 2, 3, or 4")
            except:
                print("❌ Please enter a valid number")
        print()
    
    def ask_coverage_interests(self):
        """Ask user about their coverage interests (multi-select)"""
        print("Question 3: What types of coverage are you interested in?")
        print("(You can select multiple options by entering numbers separated by commas)")
        print()
        print("1. Life Insurance")
        print("2. Health/Medicare")
        print("3. Supplemental Health")
        print("4. Retirement Income")
        print("5. Employee Benefits")
        
        while True:
            try:
                choices = input("\nEnter your choices (e.g., 1,3,4): ").strip()
                choice_list = [c.strip() for c in choices.split(',')]
                
                if all(c in ['1', '2', '3', '4', '5'] for c in choice_list):
                    coverage_mapping = {
                        '1': 'life', '2': 'health', '3': 'supplemental', 
                        '4': 'retirement', '5': 'employee_benefits'
                    }
                    selected_coverage = [coverage_mapping[c] for c in choice_list]
                    self.user_responses['coverage_interests'] = selected_coverage
                    
                    # Display selected options
                    option_names = ['Life Insurance', 'Health/Medicare', 'Supplemental Health', 'Retirement Income', 'Employee Benefits']
                    selected_names = [option_names[int(c)-1] for c in choice_list]
                    print(f"✅ Selected coverage: {', '.join(selected_names)}")
                    break
                else:
                    print("❌ Please enter valid numbers (1-5) separated by commas")
            except:
                print("❌ Please enter valid numbers separated by commas")
        print()
    
    def ask_dependents(self):
        """Ask user if they have dependents"""
        print("Question 4: Do you have dependents (spouse, children, etc.)?")
        print("1. Yes")
        print("2. No")
        
        while True:
            try:
                choice = input("\nEnter your choice (1-2): ").strip()
                if choice in ['1', '2']:
                    self.user_responses['has_dependents'] = choice == '1'
                    print(f"✅ Dependents: {'Yes' if choice == '1' else 'No'}")
                    break
                else:
                    print("❌ Please enter 1 or 2")
            except:
                print("❌ Please enter a valid number")
        print()
    
    def ask_coverage_channel(self):
        """Ask user about preferred coverage channel"""
        print("Question 5: How would you prefer to get coverage?")
        print("1. Individual/Direct purchase")
        print("2. Through employer")
        
        while True:
            try:
                choice = input("\nEnter your choice (1-2): ").strip()
                if choice in ['1', '2']:
                    channel_mapping = {'1': 'individual', '2': 'employer'}
                    self.user_responses['coverage_channel'] = channel_mapping[choice]
                    print(f"✅ Coverage channel: {'Individual' if choice == '1' else 'Through employer'}")
                    break
                else:
                    print("❌ Please enter 1 or 2")
            except:
                print("❌ Please enter a valid number")
        print()
    
    def ask_priority(self):
        """Ask user about their coverage priority"""
        print("Question 6: What's your priority when choosing coverage?")
        print("1. Low cost")
        print("2. Balanced coverage and cost")
        print("3. Maximum coverage")
        
        while True:
            try:
                choice = input("\nEnter your choice (1-3): ").strip()
                if choice in ['1', '2', '3']:
                    priority_mapping = {'1': 'low_cost', '2': 'balanced', '3': 'maximum_coverage'}
                    self.user_responses['priority'] = priority_mapping[choice]
                    print(f"✅ Priority: {['Low cost', 'Balanced', 'Maximum coverage'][int(choice)-1]}")
                    break
                else:
                    print("❌ Please enter 1, 2, or 3")
            except:
                print("❌ Please enter a valid number")
        print()
    
    def analyze_responses(self):
        """
        Analyze user responses and determine recommended brands and products
        """
        print("🔄 Analyzing your responses...")
        print()
        
        # Initialize brand scores
        brand_scores = {brand: 0 for brand in products.keys()}
        
        # Score brands based on coverage interests
        for coverage_type in self.user_responses.get('coverage_interests', []):
            for brand, data in products.items():
                if coverage_type in data['categories']:
                    brand_scores[brand] += 2  # Base score for matching coverage
        
        # Age-based prioritization
        if self.user_responses.get('age_range') == '60_plus':
            brand_scores['Colonial Penn'] += 3
            brand_scores['myHealthPolicy.com'] += 3
            brand_scores['Bankers Life'] += 2  # Also good for seniors
        
        # Employment status considerations
        if self.user_responses.get('employment_status') in ['employed', 'self_employed']:
            brand_scores['Washington National'] += 2  # Good for working adults
            brand_scores['Optavise'] += 1
        
        if self.user_responses.get('employment_status') in ['retired', 'nearing_retirement']:
            brand_scores['Bankers Life'] += 2
            brand_scores['Colonial Penn'] += 1
        
        # Coverage channel prioritization
        if self.user_responses.get('coverage_channel') == 'employer':
            brand_scores['Optavise'] += 3
            brand_scores['Washington National'] += 2
        
        # Dependents consideration
        if self.user_responses.get('has_dependents'):
            brand_scores['Bankers Life'] += 1  # Good for families
            if 'life' in self.user_responses.get('coverage_interests', []):
                brand_scores['Colonial Penn'] += 1
        
        # Priority-based adjustments
        if self.user_responses.get('priority') == 'low_cost':
            brand_scores['Colonial Penn'] += 1  # Often more affordable
        elif self.user_responses.get('priority') == 'maximum_coverage':
            brand_scores['Bankers Life'] += 1
            brand_scores['Washington National'] += 1
        
        # Select brands with scores > 0 and sort by score
        self.recommended_brands = [(brand, score) for brand, score in brand_scores.items() if score > 0]
        self.recommended_brands.sort(key=lambda x: x[1], reverse=True)
    
    def display_recommendations(self):
        """Display personalized product recommendations"""
        print("🎯 Processing complete! Here are your personalized recommendations:")
        print("=" * 70)
        print()
        
        if not self.recommended_brands:
            print("❌ I couldn't find specific matches for your criteria.")
            print("💡 I recommend speaking with a CNO Financial Group representative")
            print("   for personalized guidance on our full product portfolio.")
            return
        
        print("✅ Based on your answers, here are the best matching products:")
        print()
        
        # Display recommendations for each brand
        for i, (brand, score) in enumerate(self.recommended_brands):
            # Brand icons
            brand_icons = {
                'Bankers Life': '🏦',
                'Colonial Penn': '🏛️', 
                'Washington National': '🏥',
                'Optavise': '💼',
                'myHealthPolicy.com': '🔍'
            }
            
            icon = brand_icons.get(brand, '🏢')
            print(f"{icon} {brand}")
            print("-" * (len(brand) + 3))
            
            # Display relevant products based on user's coverage interests
            user_coverage = self.user_responses.get('coverage_interests', [])
            brand_data = products[brand]
            
            # Check if brand categories match user interests
            relevant_products = []
            for category in brand_data['categories']:
                if category in user_coverage or category == 'life' and 'life' in user_coverage:
                    relevant_products = brand_data['products']
                    break
                elif category == 'health' and 'health' in user_coverage:
                    relevant_products = brand_data['products']
                    break
                elif category == 'supplemental' and 'supplemental' in user_coverage:
                    relevant_products = brand_data['products']
                    break
                elif category == 'retirement' and 'retirement' in user_coverage:
                    relevant_products = brand_data['products']
                    break
                elif category == 'employee_benefits' and 'employee_benefits' in user_coverage:
                    relevant_products = brand_data['products']
                    break
            
            # If no specific match, show all products for highly scored brands
            if not relevant_products and score >= 3:
                relevant_products = brand_data['products']
            
            # Display products
            if relevant_products:
                for product in relevant_products:
                    print(f" • {product}")
            else:
                print(f" • Contact {brand} for product details")
            
            print()
        
        # Add closing message
        print("🌟 About CNO Financial Group:")
        print("-" * 30)
        print("Each of these brands is part of CNO Financial Group — a trusted")
        print("insurance company serving middle-income Americans with affordable")
        print("insurance and retirement solutions for over 160 years.")
        print()
        print("💡 Next Steps:")
        print("• Contact your preferred brand(s) for detailed quotes")
        print("• Speak with a licensed agent for personalized guidance") 
        print("• Visit cnofinancialgroup.com for more information")
        print()
        print("Thank you for using CNO Product Advisor! 🙏")
    
    def run_consultation(self):
        """
        Main method to run the complete consultation process
        """
        # Welcome and introduction
        self.display_welcome()
        
        # Ask all questions
        self.ask_age_range()
        self.ask_employment_status()
        self.ask_coverage_interests()
        self.ask_dependents()
        self.ask_coverage_channel()
        self.ask_priority()
        
        # Analyze and provide recommendations
        self.analyze_responses()
        self.display_recommendations()

# Main execution block
if __name__ == "__main__":
    """
    Entry point for the CNO Product Advisor chatbot
    """
    try:
        # Create and run the chatbot
        advisor = CNOProductAdvisor()
        advisor.run_consultation()
        
    except KeyboardInterrupt:
        print("\n\n👋 Thank you for using CNO Product Advisor!")
        print("Visit us anytime at cnofinancialgroup.com")
        
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try again or contact support.")