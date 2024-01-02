import google.generativeai as genai
import os

# Load dotenv
from dotenv import load_dotenv
load_dotenv()

# Set API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

prompt = input("Enter a prompt: ")

response = model.generate_content(prompt)

print(response.text)
