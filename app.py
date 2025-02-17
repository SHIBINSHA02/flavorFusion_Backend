from flask import Flask, request, jsonify
from model import get_chat_response  # Import your function

app = Flask(__name__)

@app.route('/prompt', methods=['POST'])
def generate_response():
    if request.content_type != 'application/json':  # Check Content-Type
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.get_json(silent=True)  # Get JSON safely
    if not data or "prompt" not in data:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        response = get_chat_response(data["prompt"])
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
