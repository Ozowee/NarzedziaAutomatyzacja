from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Strona - Rafał Ciach 2024 Git auto"
