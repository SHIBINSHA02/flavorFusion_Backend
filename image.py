import requests

# Function to get images from Pixabay
def get_pixabay_images(api_key, query, image_type='photo'):
    """
    Fetches images from the Pixabay API based on the search query.

    Args:
        api_key (str): Your Pixabay API key.
        query (str): The search term for the images.
        image_type (str): The type of images to fetch (default is 'photo').

    Returns:
        dict: A dictionary containing image URLs and their tags.
    """
    url = f"https://pixabay.com/api/?key={api_key}&q={query}&image_type={image_type}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching data from Pixabay: {response.status_code} - {response.text}")

    data = response.json()
    images = []
    for hit in data.get('hits', []):
        images.append({
            'webformatURL': hit['webformatURL'],
            'tags': hit['tags'].split(', ')  # Split tags into a list
        })
    
    return images  # Return list of images with their tags

def calculate_tag_proportion(images, target_tag):
    """
    Calculates the proportion of images that contain a specific tag.

    Args:
        images (list): List of images with their tags.
        target_tag (str): The tag to check for.

    Returns:
        float: The proportion of images that contain the target tag.
    """
    if not images:
        return 0.0

    total_images = len(images)
    matching_images = sum(1 for image in images if target_tag in image['tags'])

    return matching_images / total_images  # Proportion of images with the target tag