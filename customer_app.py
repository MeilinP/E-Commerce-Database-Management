import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:5000"  # Flask API URL

st.title("🛒 E-Commerce Store")

# Sidebar Navigation
menu = st.sidebar.radio("Navigation", ["Browse Products", "Cart", "Place Order", "Write a Review"])

# Store cart items in session
if "cart" not in st.session_state:
    st.session_state.cart = []

# 1️⃣ Browse Products
if menu == "Browse Products":
    st.header("📦 Available Products")
    
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code == 200:
        products = response.json()
        for product in products:
            st.subheader(f"{product['name']} - ${product['price']}")
            st.write(product["product_id"])
            if st.button(f"Add {product['name']} to Cart", key=product["product_id"]):
                st.session_state.cart.append(product)
                st.success(f"Added {product['name']} to cart!")

# 2️⃣ View Cart
elif menu == "Cart":
    st.header("🛍️ Your Shopping Cart")
    if not st.session_state.cart:
        st.write("Your cart is empty.")
    else:
        total = sum(item["price"] for item in st.session_state.cart)
        for item in st.session_state.cart:
            st.write(f"{item['name']} - ${item['price']}")
        st.write(f"**Total: ${total}**")

# 3️⃣ Place Order
elif menu == "Place Order":
    st.header("📦 Checkout")
    user_id = st.number_input("Enter Your User ID", min_value=1, step=1)
    if st.button("Place Order"):
        if not st.session_state.cart:
            st.error("Your cart is empty.")
        else:
            items = [{"product_id": p["product_id"], "quantity": 1, "price": p["price"]} for p in st.session_state.cart]
            response = requests.post(f"{BASE_URL}/orders", json={"user_id": user_id, "items": items})
            if response.status_code == 200:
                st.success("✅ Order placed successfully!")
                st.session_state.cart.clear()  # Clear cart
            else:
                st.error("Failed to place order.")

# 4️⃣ Write a Review
elif menu == "Write a Review":
    st.header("⭐ Leave a Review")
    user_id = st.number_input("User ID", min_value=1, step=1)
    product_id = st.number_input("Product ID", min_value=1, step=1)
    rating = st.slider("Rating", 1, 5)
    comment = st.text_area("Write your review")
    if st.button("Submit Review"):
        review_data = {"user_id": user_id, "product_id": product_id, "rating": rating, "comment": comment}
        response = requests.post(f"{BASE_URL}/reviews", json=review_data)
        if response.status_code == 200:
            st.success("Review submitted successfully!")
        else:
            st.error("Failed to submit review.")