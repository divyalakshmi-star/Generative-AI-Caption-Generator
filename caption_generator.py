from google import genai
from PIL import Image
GEMINI_API_KEY = "AIzaSyDWdEplB4XSJLuYmVF1JTxwJVG7N6YwCfw"
client = genai.Client(api_key = GEMINI_API_KEY)
image_path = "Dogs.jpg"
print(f"DEBUG: Trying to open file at path: {image_path}")
import os

img = Image.open(image_path)
prompt = "Generate a professional and concise caption for this image suitable for LinkedIn post. Focus on the main activity and goal of the scene."
print("--- Generating Caption... ---")
response = client.models.generate_content(
    model = 'gemini-2.5-flash' ,
    contents = [prompt , img]
)
print("\nGenerated Caption:")
print(response.text)
    
