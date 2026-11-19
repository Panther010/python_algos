"""
The Statement: 
Create a utility class DataUtils containing 
    a static method normalize_column_name(name: str) -> str 
        that converts a column name to lowercase, 
        replaces spaces with underscores, 
        and strips special characters if any.
"""
import re

class DataUtils:

    @staticmethod 
    def normalize_column_name(name: str) -> str:
        return re.sub(r"[^a-zA-Z0-9 ]", "", name).strip().lower().replace(" ", "_")

if __name__ == "__main__":
    raw_name = "User Order Amount ($)"
    print(DataUtils.normalize_column_name(raw_name))