import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# List available models
models = genai.list_models()

print("Available Gemini models:")
for model in models:
    print(model.name)
