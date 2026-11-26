"""
The Statement: 
Define a custom exception class InvalidSchemaError that inherits from Exception. 
Then, write a function check_schema(columns: list) 
that raises InvalidSchemaError if "id" is not in the column list.
"""

class InvalidSchemaError(Exception):
    pass

def check_schema(columns: list):
    if "id" not in columns:
        raise InvalidSchemaError(f"ID is missing in columns: {columns}")


columns = ["name", "email", "id"]
check_schema(columns)