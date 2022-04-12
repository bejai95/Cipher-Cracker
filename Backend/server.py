from flask import Flask, request
from json import dumps

app = Flask(__name__)

@app.route("/")
def home():
    return "This route doesn't actually do anything"

if __name__ == "__main__":
    app.run(port=0)