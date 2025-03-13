from sqlalchemy import create_engine
import pandas as pd

DATABASE_URL = "postgresql://postgres:20001113MM@localhost:5432/ecommerce_db"
engine = create_engine(DATABASE_URL)

# Test if Flask is accessing the right database
df = pd.read_sql("SELECT * FROM users;", engine)
print(df)