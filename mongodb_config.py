from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access the ecommerce database
db = client["ecommerce_db"]

# Collections
reviews_collection = db["reviews"]
logs_collection = db["logs"]