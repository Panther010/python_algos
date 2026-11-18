"""
The Problem Statement: 
Create a class StreamRecord that takes a dictionary record in its constructor 
    and stores it as an attribute data. 
    Implement a method clean_fields(self, fields_to_strip: list) 
        that iterates over the specified keys in data, 
        strips leading/trailing whitespace from string values, 
        and returns self to allow method chaining.
"""

class StreamRecord:

    def __init__(self, data: dict) -> None:
        self.data = data

    def clean_fields(self, fields_to_strip: list):
        for field in fields_to_strip:
            if field in self.data and isinstance(self.data[field], str):
                self.data[field] = self.data[field].strip()

        return self


if __name__ == "__main__":
    raw_record = {"user_id": " 42 ", "email": " alice@example.com  ", "status": "active"}
    record_obj = StreamRecord(raw_record)
    record_obj.clean_fields(["user_id", "email"])
    print(record_obj.data)