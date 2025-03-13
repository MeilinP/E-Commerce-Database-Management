from mongodb_crud import add_review, get_reviews_for_product, update_review, delete_review, log_action, get_logs_for_user
from bson import ObjectId

# ✅ Add a Review
print("\nAdding Review...")
review_id = add_review(user_id=1, product_id=101, rating=4.5, comment="Great product!")
print("✅ Review Added:", review_id)

# ✅ Get Reviews for Product
print("\nFetching Reviews for Product...")
reviews = get_reviews_for_product(101)
print("✅ Product Reviews:", reviews)

# ✅ Update Review
print("\nUpdating Review...")
update_status = update_review(review_id=ObjectId(review_id), new_rating=5.0, new_comment="Amazing product!")
print("✅ Review Updated:", update_status)

# ✅ Delete Review
print("\nDeleting Review...")
delete_status = delete_review(review_id=ObjectId(review_id))
print("✅ Review Deleted:", delete_status)

# ✅ Log User Action
print("\nLogging User Action...")
log_action(user_id=1, action="User purchased Product 101")
print("✅ Action Logged!")

# ✅ Fetch Logs for User
print("\nFetching User Logs...")
logs = get_logs_for_user(1)
print("✅ User Logs:", logs)