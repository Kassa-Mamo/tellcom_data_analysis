import pandas as pd
import sqlite3

# Path to your files
EXCEL_FILE_PATH = r"C:\Users\user\Desktop\10 acadamey - W 2\tellcom_data_analysis\Data\Field Description.xlsx"
SQL_FILE_PATH = r"C:\Users\user\Desktop\10 acadamey - W 2\tellcom_data_analysis\Data\telecom.sql"

def load_excel(file_path):
    """Load data from an Excel file."""
    return pd.read_excel(file_path)

def load_sqlite(db_path, query):
    """Load data from a SQLite database."""
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Example usage
if __name__ == "__main__":
    # Load data from Excel
    excel_data = load_excel(EXCEL_FILE_PATH)
    print(excel_data.head())
    
    # Example: Load data from SQL (replace with your query)
    query = "SELECT * FROM telecom_data;"  # Adjust table name based on the actual SQL
    sqlite_data = load_sqlite(SQL_FILE_PATH, query)
    print(sqlite_data.head())
