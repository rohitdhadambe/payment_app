from flask import Flask, request, jsonify
from flask_cors import CORS
import razorpay
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = razorpay.Client(auth=(
    os.getenv("RAZORPAY_KEY_ID"),
    os.getenv("RAZORPAY_KEY_SECRET")
))

@app.route("/create-order", methods=["POST"])
def create_order():
    data = request.json
    amount = int(data["amount"]) * 100

    order = client.order.create({
        "amount": amount,
        "currency": "INR"
    })

    return jsonify(order)

@app.route("/")
def home():
    return "Backend running"

if __name__ == "__main__":
    app.run(port=5000, debug=True)