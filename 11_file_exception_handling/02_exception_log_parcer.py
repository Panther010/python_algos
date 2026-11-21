"""
The Statement: 
Write a function parse_log_stream(file_obj) -> tuple that iterates over lines in a file object.
Wrap line parsing in a try-except block catching json.JSONDecodeError. 
Use the else clause to accumulate valid parsed records into a list, 
and use finally to record that the stream iteration concluded. 
Return a tuple of (valid_records_list, error_count).
"""
import json

def parse_log_stream(file_obj) -> tuple:
    valid_records = []
    error_count  = 0
    try:
        for line in file_obj:
            try:
                record = json.loads(line.strip())
            except json.JSONDecodeError:
                error_count += 1
            else:
                valid_records.append(record)
    finally:
        print("Completed the starem processing")

    return valid_records, error_count


import io
stream = io.StringIO('{"id": 1}\nMALFORMED_JSON\n{"id": 2}\n')
print(parse_log_stream(stream))