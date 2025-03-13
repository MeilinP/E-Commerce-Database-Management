from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.ecommerce_db

# Create collections
db.create_collection("reviews")
db.create_collection("logs")

print("✅ MongoDB Collections Created!")