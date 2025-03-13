from config import engine, Base

# Create database tables
print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")