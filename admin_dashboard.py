import streamlit as st
from db import get_db
from crud import create_user, get_all_users, delete_user, create_product, get_all_products, delete_product
from mongodb_crud import get_reviews_for_product, get_logs_for_user

st.title("🛒 E-Commerce Admin Dashboard")

# Sidebar Navigation
menu = st.sidebar.radio("Navigation", ["Users", "Products", "Orders", "Reviews & Logs"])

db = next(get_db())

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
            create_user(db, name, email, password)
            st.success(f"User {name} added!")

    # View Users
    users = get_all_users(db)
    st.subheader("Existing Users")
    for user in users:
        st.text(f"{user.user_id}: {user.name} ({user.email})")

    # Delete User
    user_id_to_delete = st.number_input("User ID to delete", min_value=1, step=1)
    if st.button("Delete User"):
        if delete_user(db, user_id_to_delete):
            st.success(f"User {user_id_to_delete} deleted!")
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
            create_product(db, product_name, description, price, stock, category)
            st.success(f"Product {product_name} added!")

    # View Products
    products = get_all_products(db)
    st.subheader("Existing Products")
    for product in products:
        st.text(f"{product.product_id}: {product.name} - ${product.price}")

    # Delete Product
    product_id_to_delete = st.number_input("Product ID to delete", min_value=1, step=1)
    if st.button("Delete Product"):
        if delete_product(db, product_id_to_delete):
            st.success(f"Product {product_id_to_delete} deleted!")
        else:
            st.error("Product not found.")

# 3️⃣ View Orders
elif menu == "Orders":
    st.header("📑 View Orders")
    st.write("🚧 (Feature Coming Soon)")

# 4️⃣ Monitor Logs & Reviews
elif menu == "Reviews & Logs":
    st.header("📝 Reviews & Logs")

    product_id = st.number_input("Enter Product ID to view reviews", min_value=1, step=1)
    if st.button("Get Reviews"):
        reviews = get_reviews_for_product(product_id)
        if reviews:
            st.write(reviews)
        else:
            st.warning("No reviews found.")

    user_id = st.number_input("Enter User ID to view logs", min_value=1, step=1)
    if st.button("Get Logs"):
        logs = get_logs_for_user(user_id)
        if logs:
            st.write(logs)
        else:
            st.warning("No logs found.")