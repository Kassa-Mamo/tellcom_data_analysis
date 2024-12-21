# scripts/sql_queries.py
# Example SQL Queries for data extraction
SELECT_ALL_QUERY = "SELECT * FROM telecom_data;"
SELECT_WITH_CONDITION_QUERY = "SELECT * FROM telecom_data WHERE call_type = 'incoming';"
AGGREGATE_QUERY = """
SELECT call_type, COUNT(*) FROM telecom_data
GROUP BY call_type;
"""

