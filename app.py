from flask import Flask, request, jsonify
from model import generate_recipe
from image import search_images

app = Flask(__name__)

@app.route('/prompt', methods=['POST'])
def generate_response():
    if request.content_type != 'application/json':  # Check Content-Type
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.get_json(silent=True)  # Get JSON safely
    if not data or "prompt" not in data:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        response = generate_recipe(data["prompt"])
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/search_images', methods=['POST'])
def search_images_endpoint():
    if request.content_type != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.get_json(silent=True)
    if not data or "query" not in data:
        return jsonify({"error": "No query provided"}), 400

    try:
        images = search_images(data["query"])
        return jsonify({"images": images})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
