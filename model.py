from together import Together
import json
import re
from dotenv import load_dotenv  # Import dotenv to load environment variables
import os  # Import os to access environment variables

# Load environment variables from .env file
load_dotenv()

# Set your API key here
API_KEY = os.getenv("API_KEY")  # Get API key from environment variable

# Initialize the client with the API key
client = Together(api_key=API_KEY)

# Example recipe output format
example_output = {
    "food_name": "Spaghetti Carbonara",
    "description": "A classic Italian pasta dish made with eggs, cheese, pancetta, and pepper, delivering a rich, creamy, and savory taste in every bite.",
    "ingredients": [
        {"name": "Spaghetti", "quantity": "200g"},
        {"name": "Eggs", "quantity": "2 large"},
    ],
    "steps": [
        {
            "index": 1,
            "description": "Boil water in a large pot, add salt, and cook spaghetti until al dente.",
            "time": "10 minutes",
            "flame": "high"
        },
        {
            "index": 2,
            "description": "While pasta cooks, sauté pancetta in olive oil until crispy and golden.",
            "time": "5 minutes",
            "flame": "mid"
        },
        
    ],
    "total_time": "22 minutes",
    "conclusion": "Great food brings people together. Enjoy this homemade delight!"
}

def extract_json(text):
    """
    Extracts a valid JSON object from a text response.
    
    Args:
        text (str): The response text containing JSON.
    
    Returns:
        dict: Parsed JSON object or an error message.
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)  # Find JSON in text
    if match:
        json_text = match.group(0)
        try:
            return json.loads(json_text)
        except json.JSONDecodeError:
            return {"error": "Extracted text is not valid JSON.", "raw_text": json_text}
    return {"error": "No JSON found in response.", "raw_text": text}

def get_chat_response(user_message):
    """
    Calls the LLaMA API with system instructions to return a structured recipe in JSON format.

    Args:
        user_message (str): The message from the user.

    Returns:
        dict: The response from the LLaMA API in JSON format.
    """
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        messages=[
            {"role": "system", "content": "You are a recipe assistant. Always respond with a JSON object in the following format. If the data or the recipe is not available then give output 'Not trained for the recipe'.If prompt is irrelevent then give output as 'I dont know'"},
            {"role": "system", "content": json.dumps(example_output, indent=2)},
            {"role": "user", "content": user_message}
        ]
    )

    model_response = response.choices[0].message.content

    return extract_json(model_response)  # Extract and parse JSON


# Example Usage
user_prompt = "biriyani"
recipe = get_chat_response(user_prompt)
print(json.dumps(recipe, indent=2))
