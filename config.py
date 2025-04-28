import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
