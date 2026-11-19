"""
The Statement:
Create a class SchemaValidator 
with a static method validate_headers(expected: list, actual: list) -> bool 
    that checks if all expected columns exist in the actual headers (order-independent, case-insensitive).
"""

class SchemaValidator:

    @staticmethod
    def validate_headers(expected: list, actual: list) -> bool:
        actual_normalised = {column.lower() for column in actual}
        
        return all(col.lower() in actual_normalised for col in expected)



if __name__ == "__main__":
    expected = ["id", "timestamp", "value"]
    actual = ["TIMESTAMP", "ID", "VALUE", "extra_col"]
    print(SchemaValidator.validate_headers(expected, actual))