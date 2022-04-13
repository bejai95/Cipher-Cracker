from flask import Flask, request
from json import dumps
from caesarHacker import caesarHacker
from transpositionHacker import transpositionHacker
from substitutionHacker import substitutionHacker

app = Flask(__name__)

@app.route("/")
def home():
    return "Please use a different route"

@app.route('/caesar', methods=['PUT'])
def caesar():
    data = request.get_json()
    return caesarHacker(data["cipherText"])

@app.route('/transposition', methods=['PUT'])
def transposition():
    data = request.get_json()
    return caesarHacker(data["cipherText"])

@app.route('/substitution', methods=['PUT'])
def substitution():
    data = request.get_json()
    return substitutionHacker(data["cipherText"])
    
if __name__ == "__main__":
    app.run(port=0)