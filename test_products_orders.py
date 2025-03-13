from db import get_db
from crud import create_product, get_product, get_all_products, update_product_stock, delete_product
from crud import create_order, get_order, get_orders_by_user, update_order_status, delete_order
from crud import create_user, create_product, create_order, get_orders_by_user
# Get a database session
db = next(get_db())

# ✅ Create a User before placing an order
print("\nCreating User...")
user = create_user(db, "Alice Johnson", "alice@example.com", "securepassword")
print("✅ User Created:", user)

# ✅ Create a Product
print("\nCreating Product...")
product = create_product(db, "Laptop", "Powerful laptop", 999.99, 10, "Electronics")
print("✅ Product Created:", product)

# ✅ Now Create an Order using the actual user_id
print("\nCreating Order...")
order = create_order(db, user_id=user.user_id, items=[{"product_id": product.product_id, "quantity": 2, "price": product.price}])
print("✅ Order Created:", order)
# Test Create Product
print("Creating Product...")
product = create_product(db, "Laptop", "Powerful laptop", 999.99, 10, "Electronics")
print("✅ Product Created:", product)

# Test Get Product
print("\nFetching Product by ID...")
fetched_product = get_product(db, product.product_id)
print("✅ Product Fetched:", fetched_product)

# Test Get All Products
print("\nFetching All Products...")
products = get_all_products(db)
print("✅ All Products:", products)

# Test Update Product Stock
print("\nUpdating Product Stock...")
updated_product = update_product_stock(db, product.product_id, 5)
print("✅ Updated Product:", updated_product)

# Test Delete Product
print("\nDeleting Product...")
delete_status = delete_product(db, product.product_id)
print("✅ Product Deleted:", delete_status)

# Test Create Order
print("\nCreating Order...")
order = create_order(db, user_id=1, items=[{"product_id": 1, "quantity": 2, "price": 999.99}])
print("✅ Order Created:", order)

# Test Get Order
print("\nFetching Order by ID...")
fetched_order = get_order(db, order.order_id)
print("✅ Order Fetched:", fetched_order)

# Test Get All Orders for a User
print("\nFetching Orders for User ID 1...")
orders = get_orders_by_user(db, 1)
print("✅ User Orders:", orders)

# Test Update Order Status
print("\nUpdating Order Status...")
updated_order = update_order_status(db, order.order_id, "shipped")
print("✅ Updated Order:", updated_order)

# Test Delete Order
print("\nDeleting Order...")
delete_status = delete_order(db, order.order_id)
print("✅ Order Deleted:", delete_status)