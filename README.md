# CNO Product Advisor & Insurance Chatbot 🤖

A comprehensive suite of insurance consultation tools for CNO Financial Group with multiple deployment options.

## 🎯 **NEW: CNO Product Advisor**

A sophisticated consultation system that asks targeted questions and provides personalized product recommendations from CNO Financial Group's complete portfolio.

### **Features:**
- **6-Question Consultation**: Age, employment, coverage interests, dependents, channel, priority
- **Smart Algorithm**: Matches user profile to appropriate brands and products
- **Personalized Recommendations**: Tailored suggestions from 5 CNO subsidiaries
- **Professional Experience**: Console-based consultation like a real advisor

### **CNO Brands Covered:**
- 🏦 **Bankers Life** - Life, retirement, health insurance
- 🏛️ **Colonial Penn** - Simplified life insurance
- 🏥 **Washington National** - Supplemental health coverage
- 💼 **Optavise** - Employee benefits solutions
- 🔍 **myHealthPolicy.com** - Medicare plans

## 🚀 Quick Demo Options

### 1. **GitHub Codespaces (Recommended)**
- Click the green "Code" button → "Codespaces" → "Create codespace"
- Automatically sets up Python environment
- Run: `python src/main.py` (Choose option 2 for CNO Product Advisor)

### 2. **Direct Console Run**
- Clone repository: `git clone https://github.com/NV942004/CNO_Test_ChatBot`
- Run: `python src/cno_product_advisor.py`

### 3. **Web Demo (GitHub Pages)**
- Visit: `https://nv942004.github.io/CNO_Test_ChatBot/`
- Interactive web interface (original chatbot)

### 4. **Google Colab**
- Open `CNO_Insurance_Chatbot_Colab.ipynb` in [Google Colab](https://colab.research.google.com)
- Interactive notebook environment

### 5. **GitHub Actions Demo**
- Check the "Actions" tab for automated demo runs
- See both chatbots in action

## 🎯 Features

- **Intent Classification**: Understands user queries
- **Product Database**: CNO Financial Group products
- **Interactive Chat**: Real-time conversation
- **Multi-Platform**: Web, Colab, Codespaces
- **Automated Testing**: CI/CD pipeline

## Project Structure

```
cno-insurance-chatbot
├── src
│   ├── chatbot
│   │   ├── __init__.py
│   │   ├── bot.py
│   │   ├── intent_classifier.py
│   │   └── response_generator.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── products.py
│   │   └── intents.py
│   └── main.py
├── tests
│   ├── __init__.py
│   ├── test_bot.py
│   └── test_products.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🎯 Features

### **CNO Product Advisor (NEW!)**
- **Intelligent Consultation**: 6 targeted questions for accurate profiling
- **Multi-Brand Coverage**: Recommendations from all 5 CNO subsidiaries
- **Personalized Results**: Algorithm matches user needs to specific products
- **Professional Experience**: Console-based advisor simulation

### **Original Insurance Chatbot**
- **Intent Classification**: Understands user queries
- **Product Database**: CNO Financial Group products
- **Interactive Chat**: Real-time conversation
- **Multi-Platform**: Web, Colab, Codespaces
- **Automated Testing**: CI/CD pipeline

## 💻 Usage Examples

### **CNO Product Advisor:**
```bash
python src/cno_product_advisor.py
```

### **Application Launcher:**
```bash
python src/main.py
# Choose option 2 for CNO Product Advisor
```

### **Original Chatbot:**
```python
from src.chatbot.bot import ChatBot
bot = ChatBot()
response = bot.get_response("What insurance do you offer?")
print(response)
```

## 🧪 Testing

```bash
python -m pytest tests/ -v
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.