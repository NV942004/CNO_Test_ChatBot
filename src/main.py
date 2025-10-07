"""
CNO Financial Group - Main Application Launcher
==============================================

This script allows users to choose between different CNO applications:
1. Original Insurance Chatbot - General conversational bot
2. CNO Product Advisor - Personalized product recommendation system
"""

def display_main_menu():
    """Display the main application menu"""
    print("=" * 60)
    print("🏦 CNO Financial Group - Application Suite")
    print("=" * 60)
    print()
    print("Welcome! Please choose an application:")
    print()
    print("1. 💬 Original Insurance Chatbot")
    print("   - General conversation about insurance")
    print("   - Basic product information")
    print("   - Interactive Q&A format")
    print()
    print("2. 🎯 CNO Product Advisor (NEW!)")
    print("   - Personalized product recommendations")
    print("   - Guided consultation process")
    print("   - Tailored brand suggestions")
    print()
    print("3. 🚪 Exit")
    print()

def run_original_chatbot():
    """Run the original insurance chatbot"""
    try:
        from chatbot.bot import ChatBot
        print("\n🤖 Starting Original Insurance Chatbot...")
        print("-" * 40)
        chatbot = ChatBot()
        chatbot.start_conversation()
    except ImportError:
        print("❌ Original chatbot not available. Please check installation.")
    except Exception as e:
        print(f"❌ Error running original chatbot: {e}")

def run_product_advisor():
    """Run the CNO Product Advisor"""
    try:
        from cno_product_advisor import CNOProductAdvisor
        advisor = CNOProductAdvisor()
        advisor.run_consultation()
    except ImportError:
        print("❌ CNO Product Advisor not available. Please check installation.")
    except Exception as e:
        print(f"❌ Error running product advisor: {e}")

def main():
    """Main application launcher"""
    while True:
        display_main_menu()
        
        try:
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == '1':
                run_original_chatbot()
                
            elif choice == '2':
                run_product_advisor()
                
            elif choice == '3':
                print("\n👋 Thank you for using CNO Financial Group applications!")
                print("Visit us at cnofinancialgroup.com")
                break
                
            else:
                print("\n❌ Please enter 1, 2, or 3")
                input("Press Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n\n👋 Thank you for using CNO Financial Group applications!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()