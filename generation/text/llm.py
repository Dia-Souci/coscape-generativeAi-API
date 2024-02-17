from langchain.chat_models import ChatOpenAI
from creds import OPENAI_API_KEY

from config import model_name

# Chatgpt
chatGPT = ChatOpenAI(model_name=model_name, temperature=1.0, openai_api_key=OPENAI_API_KEY)