from flask import Flask, request, jsonify
from model import predict_root_cause

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    log = request.json["log"]
    result = predict_root_cause(log)
    return jsonify({"root_cause": result})

if __name__ == "__main__":
    app.run(debug=True)
