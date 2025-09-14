
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
CORS(app)

# Demo user (email and hashed password for testing)
users = {
    "testuser@example.com": generate_password_hash("securePass123")
}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    hashed_password = users.get(email)
    if not hashed_password or not check_password_hash(hashed_password, password):
        return jsonify({"message": "Invalid email or password"}), 401

    # return success
    return jsonify({"message": "Login successful"}), 200

if __name__ == '__main__':
    app.run(port=5000)
