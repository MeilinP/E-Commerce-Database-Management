from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, TIMESTAMP, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config import Base

# User Model
class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())

# Product Model
class Product(Base):
    __tablename__ = "products"
    
    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10,2), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    category = Column(String(100))
    created_at = Column(TIMESTAMP, default=func.now())

# Order Model
class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"))
    total_amount = Column(DECIMAL(10,2), nullable=False)
    status = Column(String(50), default="pending")
    created_at = Column(TIMESTAMP, default=func.now())

    user = relationship("User")

# Order Items Model
class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id", ondelete="CASCADE"))
    product_id = Column(Integer, ForeignKey("products.product_id", ondelete="CASCADE"))
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10,2), nullable=False)

# Payment Model
class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id", ondelete="CASCADE"))
    status = Column(String(50), nullable=False, default="pending")
    payment_date = Column(TIMESTAMP, default=func.now())