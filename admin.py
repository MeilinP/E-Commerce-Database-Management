import streamlit as st
from db import get_db
from crud import create_user, get_all_users, delete_user, create_product, get_all_products, delete_product, get_orders
from mongodb_crud import get_reviews_for_product, get_logs_for_user

st.title("🛒 E-Commerce Admin Dashboard")

# Sidebar Navigation
menu = st.sidebar.radio("Navigation", ["Users", "Products", "Orders", "Reviews & Logs"])

# 1️⃣ Manage Users
if menu == "Users":
    st.header("👥 Manage Users")

    # Add User
    with st.form("add_user_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Add User")
        if submit:
            db = next(get_db())  # Open session inside function
            create_user(db, name, email, password)
            st.success(f"User {name} added!")
            st.experimental_rerun()  # Refresh UI

    # View Users
    db = next(get_db())  
    users = get_all_users(db)
    st.subheader("Existing Users")
    for user in users:
        st.text(f"{user.user_id}: {user.name} ({user.email})")

    # Delete User
    user_id_to_delete = st.number_input("User ID to delete", min_value=1, step=1)
    if st.button("Delete User"):
        db = next(get_db())  
        if delete_user(db, user_id_to_delete):
            st.success(f"User {user_id_to_delete} deleted!")
            st.experimental_rerun()  # Refresh UI
        else:
            st.error("User not found.")

# 2️⃣ Manage Products
elif menu == "Products":
    st.header("📦 Manage Products")

    # Add Product
    with st.form("add_product_form"):
        product_name = st.text_input("Product Name")
        description = st.text_area("Description")
        price = st.number_input("Price", min_value=0.01, step=0.01)
        stock = st.number_input("Stock", min_value=0, step=1)
        category = st.text_input("Category")
        submit_product = st.form_submit_button("Add Product")
        if submit_product:
            db = next(get_db())
            create_product(db, product_name, description, price, stock, category)
            st.success(f"Product {product_name} added!")
            st.experimental_rerun()  # Refresh UI

    # View Products
    db = next(get_db())  
    products = get_all_products(db)
    st.subheader("Existing Products")
    for product in products:
        st.text(f"{product.product_id}: {product.name} - ${product.price}")

    # Delete Product
    product_id_to_delete = st.number_input("Product ID to delete", min_value=1, step=1)
    if st.button("Delete Product"):
        db = next(get_db())  
        if delete_product(db, product_id_to_delete):
            st.success(f"Product {product_id_to_delete} deleted!")
            st.experimental_rerun()  # Refresh UI
        else:
            st.error("Product not found.")

# 3️⃣ View Orders 
elif menu == "Orders":
    st.header("📑 Manage Orders")

    db = next(get_db())  # ✅ Initialize database session before using it
    orders = get_orders(db)  # ✅ Fetch all orders

    if not orders:
        st.write("No orders found.")
    else:
        for order in orders:
            st.subheader(f"Order {order.order_id}")
            st.write(f"User ID: {order.user_id}")
            st.write(f"Total Amount: ${order.total_amount}")
            st.write(f"Status: {order.status}")

            # Option to change order status
            new_status = st.selectbox(
                f"Change Status for Order {order.order_id}",
                ["pending", "shipped", "delivered", "canceled"],
                index=["pending", "shipped", "delivered", "canceled"].index(order.status),
            )

            if st.button(f"Update Status for Order {order.order_id}"):
                from crud import update_order_status
                updated_order = update_order_status(db, order.order_id, new_status)
                if updated_order:
                    st.success(f"Order {order.order_id} updated to {new_status}")
                else:
                    st.error("Failed to update order.")

# 4️⃣ Monitor Logs & Reviews
elif menu == "Reviews & Logs":
    st.header("📝 Reviews & Logs")

    product_id = st.number_input("Enter Product ID to view reviews", min_value=1, step=1)
    if st.button("Get Reviews"):
        db = next(get_db())
        reviews = get_reviews_for_product(product_id)
        if reviews:
            st.write(reviews)
        else:
            st.warning("No reviews found.")

    user_id = st.number_input("Enter User ID to view logs", min_value=1, step=1)
    if st.button("Get Logs"):
        db = next(get_db())
        logs = get_logs_for_user(user_id)
        if logs:
            st.write(logs)
        else:
            st.warning("No logs found.")