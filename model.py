import json
from google.genai import Client  # Import Gemini API Client
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Gemini client with API key from environment variable
client = Client(api_key=os.getenv("GEMINI_API_KEY"))  # Get API key from environment variable

# Define a Pydantic model for structured dish output
class DishResponse(BaseModel):
    food_name: str
    description: str
    ingredients: list[dict]
    steps: list[dict]
    total_time: str
    conclusion: str

def generate_recipe(food_name):
    prompt = f"""Generate a recipe in JSON format for the given food name.

    The recipe should follow this schema:

    Recipe = {{
        'recipe_name': str,
        'description': str,
        'ingredients': list[{{'name': str, 'quantity': str}}],
        'steps': list[{{'index': int,'step_name': str, 'description': str, 'time': str, 'flame': str}}],
        'total_time': str,
        'conclusion': str
    }}

    Food Name: "{food_name}"

    Return: Recipe for the specified food name, including its name, description, ingredients, steps (with index, description, time, and flame), total time, and a conclusion statement."""

    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt,
    )

    return response.text