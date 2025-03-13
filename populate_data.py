from db import get_db
from crud import create_user, create_product, create_order
from sqlalchemy.orm import Session
from models import User

db: Session = next(get_db())

# ✅ Ensure User Exists Before Creating Orders
def get_or_create_user(name, email, password):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        print(f"Creating new user: {email}")
        user = create_user(db, name, email, password)
    else:
        print(f"⚠️ User already exists: {email}")
    return user

# ✅ Create Mock Users
users = [
    {"name": "Alice Johnson", "email": "alice@example.com", "password": "password123"},
    {"name": "Bob Smith", "email": "bob@example.com", "password": "securepass"},
    {"name": "Charlie Lee", "email": "charlie@example.com", "password": "letmein"}
]

print("\nCreating Users...")
user_objects = []
for user in users:
    user_obj = get_or_create_user(user["name"], user["email"], user["password"])
    user_objects.append(user_obj)

# ✅ Create Mock Products
products = [
    {"name": "Laptop", "description": "High-performance laptop", "price": 999.99, "stock": 10, "category": "Electronics"},
    {"name": "Smartphone", "description": "Latest smartphone model", "price": 699.99, "stock": 15, "category": "Electronics"},
    {"name": "Wireless Headphones", "description": "Noise-canceling headphones", "price": 199.99, "stock": 20, "category": "Accessories"}
]

print("\nCreating Products...")
product_objects = []
for product in products:
    created_product = create_product(db, product["name"], product["description"], product["price"], product["stock"], product["category"])
    product_objects.append(created_product)
    print(f"✅ Created product: {created_product.name} - ${created_product.price}")

# ✅ Create Mock Orders Using an Existing User
if user_objects:
    print("\nCreating Orders...")
    order, order_items = create_order(db, user_id=user_objects[0].user_id, items=[
        {"product_id": product_objects[0].product_id, "quantity": 1, "price": product_objects[0].price},
        {"product_id": product_objects[1].product_id, "quantity": 1, "price": product_objects[1].price}
    ])
    print(f"✅ Created order: Order ID {order.order_id} for User ID {order.user_id}")

print("\n🎯 Mock Data Inserted Successfully!")