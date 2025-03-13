from mongodb_crud import add_review, log_action

# ✅ Create Mock Reviews
print("\nAdding Mock Reviews...")
reviews = [
    {"user_id": 1, "product_id": 1, "rating": 5, "comment": "Excellent laptop, fast and reliable."},
    {"user_id": 2, "product_id": 2, "rating": 4, "comment": "Good smartphone, but battery life could be better."},
    {"user_id": 3, "product_id": 3, "rating": 5, "comment": "Best headphones I've ever used!"}
]

for review in reviews:
    review_id = add_review(review["user_id"], review["product_id"], review["rating"], review["comment"])
    print(f"✅ Review Added: User {review['user_id']} -> Product {review['product_id']}")

# ✅ Log User Actions
print("\nLogging User Actions...")
actions = [
    {"user_id": 1, "action": "Browsed Laptop"},
    {"user_id": 2, "action": "Added Smartphone to Cart"},
    {"user_id": 3, "action": "Completed Order for Headphones"}
]

for action in actions:
    log_action(action["user_id"], action["action"])
    print(f"✅ Action Logged: {action['user_id']} - {action['action']}")

print("\n🎯 Mock MongoDB Data Inserted Successfully!")