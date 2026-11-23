"""
The Statement: 
Write a function validate_config(config: dict) that checks 
if the keys "host" and "port" are present in the dictionary. 
If either is missing, explicitly raise a ValueError with a clear explanatory message.
"""

def validate_config(config: dict):
    required_keys = ["host", "port"]
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required configuration key: {key}")

config = {"host": "localhost"}
validate_config(config=config)