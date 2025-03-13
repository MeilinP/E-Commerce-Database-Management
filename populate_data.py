from db import get_db
from crud import create_user, create_product, create_order

db = next(get_db())

# ✅ Create Mock Users
users = [
    {"name": "Alice Johnson", "email": "alice@example.com", "password": "password123"},
    {"name": "Bob Smith", "email": "bob@example.com", "password": "securepass"},
    {"name": "Charlie Lee", "email": "charlie@example.com", "password": "letmein"}
]

print("\nCreating Users...")
for user in users:
    created_user = create_user(db, user["name"], user["email"], user["password"])
    if created_user:
        print(f"✅ Created user: {created_user.name} - {created_user.email}")
    else:
        print(f"⚠️ User already exists: {user['email']}")

# ✅ Create Mock Products
products = [
    {"name": "Laptop", "description": "High-performance laptop", "price": 999.99, "stock": 10, "category": "Electronics"},
    {"name": "Smartphone", "description": "Latest smartphone model", "price": 699.99, "stock": 15, "category": "Electronics"},
    {"name": "Wireless Headphones", "description": "Noise-canceling headphones", "price": 199.99, "stock": 20, "category": "Accessories"}
]

print("\nCreating Products...")
for product in products:
    created_product = create_product(db, product["name"], product["description"], product["price"], product["stock"], product["category"])
    print(f"✅ Created product: {created_product.name} - ${created_product.price}")

# ✅ Create Mock Orders
print("\nCreating Orders...")
order = create_order(db, user_id=1, items=[
    {"product_id": 1, "quantity": 1, "price": 999.99},
    {"product_id": 2, "quantity": 1, "price": 699.99}
])
print(f"✅ Created order: Order ID {order.order_id} for User ID {order.user_id}")

print("\n🎯 Mock Data Inserted Successfully!")