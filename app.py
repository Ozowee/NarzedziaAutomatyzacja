from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Strona - Rafał Ciach"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
