from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=ENV_PATH)

def get_llm():
    # Ensure GROQ_API_KEY is set in your environment
    return init_chat_model("openai/gpt-oss-120b",
                      model_provider="openai",
                      base_url="https://api.groq.com/openai/v1",
                      api_key=os.getenv("GROQ_API_KEY"))
