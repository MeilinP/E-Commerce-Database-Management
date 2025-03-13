from config import SessionLocal

# Dependency to get a new session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()