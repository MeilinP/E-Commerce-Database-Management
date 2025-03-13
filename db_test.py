import psycopg2
from pymongo import MongoClient

# PostgreSQL Connection Test
try:
    conn = psycopg2.connect(
        dbname="ecommerce_db",
        user="postgres",
        password="20001113MM",  # Change this to your actual password
        host="localhost",
        port="5432"
    )
    print("✅ Connected to PostgreSQL!")
    conn.close()
except Exception as e:
    print(f"❌ PostgreSQL connection failed: {e}")

# MongoDB Connection Test
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client.ecommerce_db
    print("✅ Connected to MongoDB!")
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")