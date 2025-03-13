from db import get_db
from crud import create_user, get_user
from crud import create_product, get_product, get_all_products, update_product_stock, delete_product
from crud import create_order, get_order, get_orders_by_user, update_order_status, delete_order

# Get a database session
db = next(get_db())

# ✅ Ensure User Exists Before Creating Order
test_email = "testuser@example.com"
test_name = "Test User"
test_password = "testpassword123"

print("\nChecking if test user exists...")
user = get_user(db, 1)  # Try fetching user ID 1
if not user:
    print("Creating Test User...")
    user = create_user(db, test_name, test_email, test_password)
    print("✅ User Created:", user)
else:
    print(f"⚠️ User ID {user.user_id} already exists. Using it for testing.")

# ✅ Test Create Product
print("\nCreating Test Product...")
product = create_product(db, "Test Laptop", "Test description", 999.99, 5, "Test Category")
print("✅ Product Created:", product)

# ✅ Test Get Product
print("\nFetching Product by ID...")
fetched_product = get_product(db, product.product_id)
print("✅ Product Fetched:", fetched_product)

# ✅ Test Get All Products
print("\nFetching All Products...")
products = get_all_products(db)
print("✅ All Products Count:", len(products))

# ✅ Test Update Product Stock
print("\nUpdating Product Stock...")
updated_product = update_product_stock(db, product.product_id, 10)
print("✅ Updated Product Stock:", updated_product)

# ✅ Test Delete Product
print("\nDeleting Product...")
delete_status = delete_product(db, product.product_id)
print("✅ Product Deleted:", delete_status)

# ✅ Test Create Order (Now using a valid user)
print("\nCreating Test Order...")
order = create_order(db, user.user_id, items=[{"product_id": product.product_id, "quantity": 2, "price": 999.99}])
print("✅ Order Created:", order)

# ✅ Test Get Order
print("\nFetching Order by ID...")
fetched_order = get_order(db, order.order_id)
print("✅ Order Fetched:", fetched_order)

# ✅ Test Get All Orders for User
print("\nFetching Orders for User ID 1...")
orders = get_orders_by_user(db, user.user_id)
print("✅ User Orders Count:", len(orders))

# ✅ Test Update Order Status
print("\nUpdating Order Status...")
updated_order = update_order_status(db, order.order_id, "shipped")
print("✅ Updated Order:", updated_order)

# ✅ Test Delete Order
print("\nDeleting Order...")
delete_status = delete_order(db, order.order_id)
print("✅ Order Deleted:", delete_status)