import openai
import json
import re
from dotenv import load_dotenv  # Import dotenv to load environment variables
import os  # Import os to access environment variables

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key here
API_KEY = os.getenv("API_KEY_open")  # Get OpenAI API key from environment variable

# Example recipe output format
example_output = {
    "food_name": "Spaghetti Carbonara",
    "description": "A classic Italian pasta dish made with eggs, cheese, pancetta, and pepper, delivering a rich, creamy, and savory taste in every bite.",
    "ingredients": [
        {"name": "Spaghetti", "quantity": "200g"},
        {"name": "Eggs", "quantity": "2 large"},
        {"name": "Parmesan Cheese", "quantity": "50g"},
        {"name": "Pancetta", "quantity": "100g"},
        {"name": "Black Pepper", "quantity": "1 tsp"},
        {"name": "Salt", "quantity": "to taste"},
        {"name": "Olive Oil", "quantity": "1 tbsp"}
    ],
    "steps": [
        {"index": 1, "description": "Boil water in a large pot, add salt, and cook spaghetti until al dente.", "time": "10 minutes", "flame": "high"},
        {"index": 2, "description": "While pasta cooks, sauté pancetta in olive oil until crispy and golden.", "time": "5 minutes", "flame": "mid"},
        {"index": 3, "description": "Whisk eggs with grated Parmesan cheese and black pepper in a bowl.", "time": "2 minutes", "flame": "null"},
        {"index": 4, "description": "Drain spaghetti and mix immediately with pancetta. Remove from heat.", "time": "2 minutes", "flame": "low"},
        {"index": 5, "description": "Quickly mix the pasta with the egg mixture to create a creamy sauce.", "time": "2 minutes", "flame": "null"},
        {"index": 6, "description": "Serve immediately with extra Parmesan and black pepper.", "time": "1 minute", "flame": "null"}
    ],
    "total_time": "22 minutes",
    "conclusion": "Great food brings people together. Enjoy this homemade delight!"
}

def extract_json(text):
    """
    Extracts a valid JSON object from a text response.
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        json_text = match.group(0)
        try:
            return json.loads(json_text)
        except json.JSONDecodeError:
            return {"error": "Extracted text is not valid JSON.", "raw_text": json_text}
    return {"error": "No JSON found in response.", "raw_text": text}

def get_chat_response(user_message):
    """
    Calls the OpenAI ChatGPT API to return a structured recipe in JSON format.
    """
    openai.api_key = API_KEY  # Use the API key from the environment variable
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" or "gpt-3.5-turbo" depending on your plan
        messages=[
            {"role": "system", "content": "You are a recipe assistant. Always respond with a JSON object in the following format. If the data or the recipe is not available then give output 'Not trained for the recipe'. If the prompt is irrelevant then give output as 'I don't know'."},
            {"role": "system", "content": json.dumps(example_output, indent=2)},
            {"role": "user", "content": user_message}
        ]
    )
    
    model_response = response["choices"][0]["message"]["content"]
    return extract_json(model_response)

# Example Usage
user_prompt = "juice"
recipe = get_chat_response(user_prompt)
print(json.dumps(recipe, indent=2))