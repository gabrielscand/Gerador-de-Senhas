from flask import Flask, jsonify, request
from flask_cors import CORS
from utils.password_generator import generate_password

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["GET"])
def generate():
    length = int(request.args.get("length", 12))
    use_upper = request.args.get("upper", "true").lower() == "true"
    use_lower = request.args.get("lower", "true").lower() == "true"
    use_digits = request.args.get("digits", "true").lower() == "true"
    use_symbols = request.args.get("symbols", "true").lower() == "true"

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    return jsonify({"password": password})


if __name__ == "__main__":
    app.run(debug=True)
