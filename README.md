# Chainlit Chatbot with Gemini AI

## Overview
This project is a chatbot built using **Chainlit** and **Google Gemini AI**. The chatbot maintains a conversation history and interacts with users by processing their messages and generating responses using **LangChain's Google Generative AI integration**.

## Features
- Uses **Chainlit** for the chatbot interface.
- Integrates with **Google Gemini AI (gemini-1.5-flash)** for natural language processing.
- Maintains **conversation history** for contextual responses.
- Supports **system instructions** to control chatbot behavior.


## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/paravsyal02/Zomato-Chatbot-with-Chainlit.git
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up API Keys
- Ensure you have a **Google Gemini API Key**.
- Set up the API key as an environment variable:
  ```sh
  export GOOGLE_API_KEY='your-api-key-here'  # Linux/Mac
  set GOOGLE_API_KEY='your-api-key-here'     # Windows
  ```

## Usage
### 1. Initialize the Chatbot
```sh
chainlit init
```

### 2. Run the Chatbot
```sh
chainlit run app.py
```

### 3. Interacting with the Chatbot
- Open the provided **localhost URL** in your browser.
- Type messages and interact with Gemini AI.

## Code Explanation
### **app.py (Main Chatbot Logic)**
- Listens for user messages.
- Appends messages to the conversation history.
- Calls `ask_order()` from `llm.py` to get a response.
- Sends the response back to the user via Chainlit UI.

### **llm.py (LLM Integration)**
- Loads the Gemini AI model using **LangChain**.
- Sends user messages along with system instructions.
- Receives and returns a response from Gemini.

### **prompt.py (System Instructions)**
- Contains predefined chatbot behavior guidelines.
- Example: "You are a helpful food-ordering assistant."

## Troubleshooting
### 1. **Chainlit Markdown (`chainlit.md`) Not Loading?**
- Try adding this to `app.py` before sending the first message:
  ```python
  system_prompt = cl.get_prompt()  # Fetches markdown content
  await cl.Message(content=system_prompt).send()
  ```

### 2. **Environment Issues?**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check if the correct Python version (>=3.8) is being used.

## Contributing
Feel free to submit pull requests or report issues!

## License
This project is open-source and licensed under the MIT License.

