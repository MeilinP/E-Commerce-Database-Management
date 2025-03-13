from sqlalchemy.orm import Session
from models import User
from werkzeug.security import generate_password_hash
from models import Product
from models import Order, OrderItem
from config import SessionLocal  # ✅ Import SessionLocal to use in functions
# Create a new user
def create_user(db: Session, name: str, email: str, password: str):
    hashed_password = generate_password_hash(password)
    new_user = User(name=name, email=email, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Create a new product
def create_product(db: Session, name: str, description: str, price: float, stock: int, category: str):
    new_product = Product(name=name, description=description, price=price, stock=stock, category=category)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
# Fetch a user by ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()
# Fetch all users
def get_all_users(db: Session):
    return db.query(User).all()
# Update a user's name
def update_user(db: Session, user_id: int, new_name: str):
    user = db.query(User).filter(User.user_id == user_id).first()
    if user:
        user.name = new_name
        db.commit()
        return user
    return None
# Delete a user
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.user_id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

# Fetch a product by ID
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.product_id == product_id).first()
# Fetch all products
def get_all_products(db: Session):
    return db.query(Product).all()
# Update product stock
def update_product_stock(db: Session, product_id: int, new_stock: int):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if product:
        product.stock = new_stock
        db.commit()
        return product
    return None
# Delete a product
def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return True
    return False

# Create a new order
def create_order(db: Session, user_id: int, items: list):
    print(f"Checking user_id: {user_id}")  # Debugging
    user_exists = db.query(User).filter(User.user_id == user_id).first()
    
    if not user_exists:
        print(f"ERROR: User ID {user_id} not found!")
        return {"error": "User not found"}

    total_amount = sum(item["quantity"] * item["price"] for item in items)
    new_order = Order(user_id=user_id, total_amount=total_amount, status="pending")
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for item in items:
        order_item = OrderItem(order_id=new_order.order_id, product_id=item["product_id"], quantity=item["quantity"], price=item["price"])
        db.add(order_item)

    db.commit()
    print(f"Order {new_order.order_id} placed successfully!")
    return new_order
# Fetch an order by ID
def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.order_id == order_id).first()
# Fetch all orders for a user
def get_orders_by_user(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id).all()
# Update order status
def update_order_status(db: Session, order_id: int, new_status: str):
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if order:
        order.status = new_status
        db.commit()
        return order
    return None
# Delete an order
def delete_order(db: Session, order_id: int):
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if order:
        db.query(OrderItem).filter(OrderItem.order_id == order_id).delete()  # ✅ Delete items first
        db.delete(order)
        db.commit()
        return True
    return False
# Fetch all orders
def get_orders(db: Session):
    return db.query(Order).all()