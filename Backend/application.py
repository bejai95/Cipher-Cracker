from flask import Flask, request
from json import dumps
from caesarHacker import caesarHacker
from transpositionHacker import transpositionHacker
from substitutionHacker import substitutionHackerPartial, substitutionHackerFull
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

@application.route("/")
def home():
    return "This is just the home route, it doesn't actually do anything. Please use a different route."

@application.route('/caesar', methods=['PUT'])
def caesar():
    data = request.get_json()
    return dumps(caesarHacker(data["cipherText"]))

@application.route('/transposition', methods=['PUT'])
def transposition():
    data = request.get_json()
    return dumps(transpositionHacker(data["cipherText"]))

@application.route('/substitution', methods=['PUT'])
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

@application.route('/unknown', methods=['PUT'])
def unknown():
    data = request.get_json()

    caesar = caesarHacker(data["cipherText"])
    if "message" not in caesar.keys():
        return dumps({
            "result": caesar,
            "cipherType": "caesar"
        })

    transposition = transpositionHacker(data["cipherText"])
    if "message" not in transposition.keys():
        return dumps({
            "result": transposition,
            "cipherType": "transposition"
        })

    substitution = substitutionHackerPartial(data["cipherText"])
    return dumps({
        "result": substitution,
        "cipherType": "substitution"
    })
   
if __name__ == "__main__":
    application.run()