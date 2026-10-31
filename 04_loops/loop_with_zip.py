"""
Scenario: 
Your ingestion pipeline receives a list of column names from a header row and 
a separate list of corresponding data types from a database schema definition. 
You need to combine them into a schema mapping.
"""


# Test data
cols = ["user_id", "signup_date", "is_active"]
types = ["INT", "TIMESTAMP", "BOOLEAN"]

def create_schema_map(columns: list[str], data_types: list[str]) -> dict:
    result = {}

    for key, val in zip(columns, data_types):
        result[key] = val

    return result

print(create_schema_map(cols, types))