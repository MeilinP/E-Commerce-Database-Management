from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy.orm import Session
from config import SessionLocal
from models import User, Product, Order
from crud import create_user, create_product, create_order
from mongodb_crud import add_review, get_reviews_for_product, log_action

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.route("/")
def home():
    return jsonify({"message": "E-Commerce API is running!"})

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/users", methods=["POST"])
def register_user():
    data = request.json
    db = next(get_db())
    user = create_user(db, data["name"], data["email"], data["password"])
    return jsonify({"user_id": user.user_id, "name": user.name, "email": user.email})
@app.route("/products", methods=["POST"])
def add_product():
    data = request.json
    db = next(get_db())
    product = create_product(db, data["name"], data["description"], data["price"], data["stock"], data["category"])
    return jsonify({"product_id": product.product_id, "name": product.name, "price": product.price})
@app.route("/products", methods=["GET"])
def get_products():
    db = next(get_db())
    products = db.query(Product).all()
    return jsonify([{"product_id": p.product_id, "name": p.name, "price": p.price} for p in products])
@app.route("/orders", methods=["POST"])
def place_order():
    data = request.json
    db = next(get_db())
    order = create_order(db, data["user_id"], data["items"])
    return jsonify({"order_id": order.order_id, "status": order.status, "total_amount": str(order.total_amount)})
@app.route("/reviews", methods=["POST"])
def submit_review():
    data = request.json
    review_id = add_review(data["user_id"], data["product_id"], data["rating"], data["comment"])
    return jsonify({"message": "Review added", "review_id": str(review_id)})
@app.route("/reviews/<int:product_id>", methods=["GET"])
def get_reviews(product_id):
    reviews = get_reviews_for_product(product_id)
    return jsonify(reviews)
@app.route("/logs", methods=["POST"])
def log_user_action():
    data = request.json
    log_action(data["user_id"], data["action"])
    return jsonify({"message": "User action logged!"})