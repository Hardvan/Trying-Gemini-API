import google.generativeai as genai
import PIL.Image
import os

# Load dotenv
from dotenv import load_dotenv
load_dotenv()

# Set API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

img = PIL.Image.open('apple.jpg')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro-vision')

response = model.generate_content(["what is the total calorie count?", img])

print(response.text)
