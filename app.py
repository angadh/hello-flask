# ----------------------------
# 1. app.py
# ----------------------------
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World from Flask + Gunicorn + Nginx!"
