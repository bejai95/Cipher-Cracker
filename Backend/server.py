from tkinter import EXCEPTION
from flask import Flask, request
from json import dumps
from caesarHacker import caesarHacker
from transpositionHacker import transpositionHacker
from substitutionHacker import substitutionHackerPartial, substitutionHackerFull

app = Flask(__name__)

@app.route("/")
def home():
    return "Please use a different route"

@app.route('/caesar', methods=['PUT'])
def caesar():
    data = request.get_json()
    return dumps(caesarHacker(data["cipherText"]))

@app.route('/transposition', methods=['PUT'])
def transposition():
    data = request.get_json()
    return dumps(caesarHacker(data["cipherText"]))

@app.route('/substitution', methods=['PUT'])
def substitution():
    data = request.get_json()
    
    mode = request.args.get("mode")
    if mode == "partial":
        return dumps(substitutionHackerPartial(data["cipherText"]))
    elif mode == "full":
        if "intersectedMapping" not in data.keys():
            raise Exception("intersectedMapping argument was not provided")
        else:
            return dumps(substitutionHackerFull(data["cipherText"], data["intersectedMapping"]))
    else:
        raise Exception("mode paramater incorrect or missing")
        

    
    


    
    


if __name__ == "__main__":
    app.run(port=2000)