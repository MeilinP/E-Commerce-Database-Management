from mongodb_config import reviews_collection
from datetime import datetime

# Add a new product review
def add_review(user_id: int, product_id: int, rating: float, comment: str):
    review = {
        "user_id": user_id,
        "product_id": product_id,
        "rating": rating,
        "comment": comment,
        "timestamp": datetime.utcnow()
    }
    result = reviews_collection.insert_one(review)
    return result.inserted_id
# Fetch reviews for a specific product
def get_reviews_for_product(product_id: int):
    return list(reviews_collection.find({"product_id": product_id}))
# Update a review's rating or comment
def update_review(review_id, new_rating=None, new_comment=None):
    update_data = {}
    if new_rating is not None:
        update_data["rating"] = new_rating
    if new_comment is not None:
        update_data["comment"] = new_comment

    result = reviews_collection.update_one({"_id": review_id}, {"$set": update_data})
    return result.modified_count
# Delete a review by ID
def delete_review(review_id):
    result = reviews_collection.delete_one({"_id": review_id})
    return result.deleted_count
from mongodb_config import logs_collection

# Log user actions (e.g., "User viewed product", "User placed an order")
def log_action(user_id: int, action: str):
    log_entry = {
        "user_id": user_id,
        "action": action,
        "timestamp": datetime.utcnow()
    }
    logs_collection.insert_one(log_entry)
# Fetch logs for a specific user
def get_logs_for_user(user_id: int):
    return list(logs_collection.find({"user_id": user_id}))