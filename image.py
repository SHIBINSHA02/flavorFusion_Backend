# image.py
from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def search_images(query):
  params = {
      "engine": "bing_images",
      "q": query,
      "api_key": os.getenv("SERPAPI_API_KEY")  # Get API key from environment variable
  }

  search = GoogleSearch(params)
  results = search.get_dict()
  images_results = results.get("images_results", [])
  return images_results