import requests
from dotenv import load_dotenv
import os
import asyncio
import io
from PIL import Image
import random
import string


load_dotenv()
huggingfacehub_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

async def generate_image(prompt):
    print("Generate image called")
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": f"Bearer {huggingfacehub_api_key}"}
    
    payload = {
        "inputs": prompt
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def generate_random_word(length):
    # Define the alphabet (lowercase letters)
    alphabet = string.ascii_lowercase
    
    # Generate a random word by selecting random letters from the alphabet
    random_word = ''.join(random.choice(alphabet) for _ in range(length))
    
    return random_word

async def save_image(image_bytes):
    print("save image called")
    
    filename = generate_random_word(5)

    image = Image.open(io.BytesIO(image_bytes))
    image.save(fp=f"./static/{filename}.jpeg")
    return filename