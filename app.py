from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running!"

# Intentionally vulnerable endpoint for ZAP
@app.route("/search")
def search():
    q = request.args.get("q", "")
    return f"<h1>Search result for: {q}</h1>"

# Intentionally bad code for SonarQube
@app.route("/ping")
def ping():
    password = "admin123"   # hardcoded secret
    if password == "admin123":
        return jsonify({"message": "pong"})
    return jsonify({"message": "fail"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)