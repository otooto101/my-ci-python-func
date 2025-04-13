from flask import Flask
from calculator import add, subtract

app = Flask(__name__)

@app.route("/")
def home():
    return f"Add: {add(2, 3)}, Subtract: {subtract(5, 1)}"

if __name__ == "__main__":
    app.run()
