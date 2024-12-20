# scripts/load_data.py
import pandas as pd
from sqlalchemy import create_engine

def load_data(database_url, query):
    """Load data from PostgreSQL database into a Pandas DataFrame"""
    engine = create_engine(database_url)
    df = pd.read_sql(query, engine)
    return df

# Example usage:
if __name__ == "__main__":
    DATABASE_URL = "postgresql://username:password@localhost:5432/dbname"
    QUERY = "SELECT * FROM xdr_records;"
    data = load_data(DATABASE_URL, QUERY)
    print(data.head())
