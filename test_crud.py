from db import get_db
from crud import create_user, get_user, get_all_users, update_user, delete_user

# Get a database session
db = next(get_db())

# Test Create User
print("Creating User...")
user = create_user(db, "Alice Johnson", "alice@example.com", "securepassword")
print("✅ User Created:", user)

# Test Get User
print("\nFetching User by ID...")
fetched_user = get_user(db, user.user_id)
print("✅ User Fetched:", fetched_user)

# Test Get All Users
print("\nFetching All Users...")
users = get_all_users(db)
print("✅ All Users:", users)

# Test Update User
print("\nUpdating User Name...")
updated_user = update_user(db, user.user_id, "Alice J.")
print("✅ Updated User:", updated_user)

# Test Delete User
print("\nDeleting User...")
delete_status = delete_user(db, user.user_id)
print("✅ User Deleted:", delete_status)