# CNO Insurance Chatbot 🤖

A comprehensive chatbot for CNO Financial Group insurance products and services with multiple deployment options.

## 🚀 Quick Demo Options

### 1. GitHub Codespaces (Recommended)
- Click the green "Code" button → "Codespaces" → "Create codespace"
- Automatically sets up Python environment
- Run: `python src/main.py`

### 2. Web Demo (GitHub Pages)
- Visit: `https://[your-username].github.io/cno-insurance-chatbot/`
- Interactive web interface
- No installation required

### 3. Google Colab
- Open `CNO_Insurance_Chatbot_Colab.ipynb` in [Google Colab](https://colab.research.google.com)
- Click "Runtime" → "Run All"
- Interactive notebook environment

### 4. GitHub Actions Demo
- Check the "Actions" tab for automated demo runs
- See chatbot responses in action logs

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

## 💻 Local Installation

```bash
git clone https://github.com/[your-username]/cno-insurance-chatbot
cd cno-insurance-chatbot
pip install -r requirements.txt
python src/main.py
```

## 🔧 Usage Examples

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