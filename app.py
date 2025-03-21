from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy.orm import Session
from config import SessionLocal
from models import User, Product, Order
from crud import create_user, get_all_users, create_product, create_order
from mongodb_crud import add_review, get_reviews_for_product, log_action
from bson import ObjectId  # For MongoDB ObjectId serialization

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

# ✅ GET /users
@app.route("/users", methods=["GET"])
def get_users():
    db = SessionLocal()
    users = get_all_users(db)
    db.close()
    return jsonify([{"user_id": u.user_id, "name": u.name, "email": u.email} for u in users])

# ✅ POST /users
@app.route("/users", methods=["POST"])
def register_user():
    data = request.json
    db = SessionLocal()
    user = create_user(db, data["name"], data["email"], data["password"])
    db.close()
    return jsonify({"user_id": user.user_id, "name": user.name, "email": user.email})

# ✅ POST /products
@app.route("/products", methods=["POST"])
def add_product():
    data = request.json
    db = SessionLocal()
    product = create_product(db, data["name"], data["description"], data["price"], data["stock"], data["category"])
    db.close()
    return jsonify({"product_id": product.product_id, "name": product.name, "price": product.price})

# ✅ GET /products
@app.route("/products", methods=["GET"])
def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return jsonify([{"product_id": p.product_id, "name": p.name, "price": p.price} for p in products])

# ✅ POST /orders
@app.route("/orders", methods=["POST"])
def place_order():
    data = request.json
    db = SessionLocal()
    order = create_order(db, data["user_id"], data["items"])
    db.close()
    return jsonify({"order_id": order.order_id, "status": order.status, "total_amount": str(order.total_amount)})

# ✅ GET /orders
@app.route("/orders", methods=["GET"])
def get_orders():
    db = SessionLocal()
    orders = db.query(Order).all()
    db.close()
    return jsonify([
        {"order_id": o.order_id, "user_id": o.user_id, "total_amount": str(o.total_amount), "status": o.status}
        for o in orders
    ])

# ✅ POST /reviews
@app.route("/reviews", methods=["POST"])
def submit_review():
    data = request.json
    review_id = add_review(data["user_id"], data["product_id"], data["rating"], data["comment"])
    return jsonify({"message": "Review added", "review_id": str(review_id)})

# ✅ GET /reviews/<product_id>
@app.route("/reviews/<int:product_id>", methods=["GET"])
def get_reviews_for_product_id(product_id):
    reviews = get_reviews_for_product(product_id)
    
    # Ensure MongoDB's ObjectId is serialized
    def serialize_review(review):
        review["_id"] = str(review["_id"]) if "_id" in review else None
        return review
    
    return jsonify([serialize_review(r) for r in reviews])

# ✅ POST /logs
@app.route("/logs", methods=["POST"])
def log_user_action():
    data = request.json
    log_action(data["user_id"], data["action"])
    return jsonify({"message": "User action logged!"})
@app.route("/test_add_user")
def test_add_user():
    db = SessionLocal()
    user = User(name="Debug User", email="debug@example.com", password_hash="test")
    db.add(user)
    db.commit()
    return {"message": "User added", "user_id": user.user_id}
if __name__ == "__main__":
    app.run(debug=True)