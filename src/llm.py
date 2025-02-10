from langchain_google_genai import ChatGoogleGenerativeAI
from src.prompt import system_instruction

messages = [
    {"role": "system", "content": system_instruction}
]

def ask_order(messages, model="gemini-1.5-flash", temperature=0):
    chat_model = ChatGoogleGenerativeAI(model=model, temperature=temperature)
    response = chat_model.invoke(messages)
    return response.content


