from db import get_db
from crud import create_user, get_user, get_all_users, update_user, delete_user

# Get a database session
db = next(get_db())

# Define test user details (Ensuring uniqueness)
test_email = "testuser@example.com"
test_name = "Test User"
test_password = "testpassword123"

# ✅ Check if User Already Exists Before Creating
existing_user = get_user(db, 1)  # Try fetching user ID 1
if existing_user:
    print(f"⚠️ User ID {existing_user.user_id} already exists. Using it for testing.")
    user = existing_user
else:
    print("Creating Test User...")
    user = create_user(db, test_name, test_email, test_password)
    print("✅ User Created:", user)

# ✅ Test Get User by ID
print("\nFetching User by ID...")
fetched_user = get_user(db, user.user_id)
print("✅ User Fetched:", fetched_user)

# ✅ Test Get All Users
print("\nFetching All Users...")
users = get_all_users(db)
print("✅ All Users Count:", len(users))

# ✅ Test Update User Name
print("\nUpdating User Name...")
updated_user = update_user(db, user.user_id, "Updated Test User")
print("✅ Updated User:", updated_user)

# ✅ Test Delete User
print("\nDeleting User...")
delete_status = delete_user(db, user.user_id)
print("✅ User Deleted:", delete_status)