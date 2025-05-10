# QnA Chatbot

A simple and interactive QnA chatbot built with LangChain, Streamlit, and Ollama. This chatbot allows users to interact with different AI models through a user-friendly web interface.

## Features

- Interactive chat interface using Streamlit
- Support for multiple AI models (Gemma, Llama, Mistral)
- Real-time chat history
- Download chat history functionality
- Clean and modern UI design
- Environment variable support for API keys

## Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally
- Git (for cloning the repository)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Jit017/simpleqnachatbot.git
cd simpleqnachatbot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your API keys:
```
LANGCHAIN_API_KEY=your_api_key_here
LANGCHAIN_PROJECT=qnachatbot
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Select your preferred AI model from the sidebar
4. Start chatting with the AI assistant!

## Available Models

- gemma2:2b
- llama3
- mistral

## Features

- **Model Selection**: Choose from different AI models in the sidebar
- **Chat History**: View your conversation history
- **Download Chat**: Save your chat history as a text file
- **Clear Chat**: Reset the conversation at any time

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 