"""
The Statement: 
Write a function read_config_file(filepath: str) -> str that attempts to open and read a file.
Use except FileNotFoundError to return a default string "DEFAULT_CONFIG", 
use else to return the actual file contents if successful, 
and use finally to ensure a print statement or debug hook logs that the operation completed.
"""
def read_config_file(filepath: str) -> str:
    try:
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Give file {filepath} does not exists")
        return "DEFAULT_CONFIG"
    else:
        return content
    finally:
        print("Completed read and file processing")

print(read_config_file("/Users/bakulseth/PycharmProjects/ai_journy/python_algos/requirements.txt"))