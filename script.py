import zipfile
import os

# Prepare the React frontend and Node.js backend folder structure with example files
frontend_code = '''
// App.js sample for login page
import React, { useState } from 'react';
import './App.css';

function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      const res = await fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      });
      const data = await res.json();
      if (res.ok) {
        alert('Login successful!');
      } else {
        setError(data.message || 'Login failed');
      }
    } catch (err) {
      setError('Server error');
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h2>Login to DataSecure</h2>
      <form onSubmit={handleSubmit} className="login-form">
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          minLength={6}
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Logging in...' : 'Login'}
        </button>
        {error && <div className="error">{error}</div>}
      </form>
    </div>
  );
}

export default App;
'''

frontend_css = '''
/* App.css */
.App {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  max-width: 400px;
  margin: 5rem auto;
  padding: 2rem;
  box-shadow: 0 0 10px rgba(0,0,0,0.15);
  border-radius: 8px;
  background: #1a1a1a;
  color: white;
}
.login-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.login-form input {
  padding: 0.75rem;
  border-radius: 5px;
  border: none;
  font-size: 1rem;
}
.login-form button {
  cursor: pointer;
  padding: 0.8rem;
  background: #4CAF50;
  color: white;
  font-weight: 700;
  border: none;
  border-radius: 5px;
  transition: background 0.3s ease;
}
.login-form button:hover {
  background: #45a049;
}
.error {
  color: #ff4d4f;
  font-weight: 600;
}
'''

backend_code = '''
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
'''

# Create folder structure and files
os.makedirs('DataSecureFrontend/src', exist_ok=True)
os.makedirs('DataSecureBackend', exist_ok=True)

with open('DataSecureFrontend/src/App.js', 'w') as f:
    f.write(frontend_code)

with open('DataSecureFrontend/src/App.css', 'w') as f:
    f.write(frontend_css)

with open('DataSecureBackend/app.py', 'w') as f:
    f.write(backend_code)

# Create ZIP package
zip_filename = 'datasecure_software_package.zip'
with zipfile.ZipFile(zip_filename, 'w') as zf:
    zf.write('DataSecureFrontend/src/App.js')
    zf.write('DataSecureFrontend/src/App.css')
    zf.write('DataSecureBackend/app.py')

zip_filename
