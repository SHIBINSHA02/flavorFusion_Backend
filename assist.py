import openai
import os  # Import os to access environment variables
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key here
API_KEY = os.getenv("API_KEY_open")  # Get OpenAI API key from environment variable

def chat_with_assistant(user_input):
    """Simple AI assistant using OpenAI API"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can change to "gpt-3.5-turbo" for a cheaper option
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_input}
        ],
        api_key=API_KEY  # Use the API key from the environment variable
    )
    return response["choices"][0]["message"]["content"]

# Example usage
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Assistant: Goodbye!")
            break
        response = chat_with_assistant(user_input)
        print("Assistant:", response)
