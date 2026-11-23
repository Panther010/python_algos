"""
The Statement: 
Write a function ingest_payload(payload: list, max_size: int) 
that raises a TypeError if payload is not a list, 
and raises an OverflowError if len(payload) > max_size.
"""

def ingest_payload(payload: list, max_size: int):
    if not isinstance(payload, list):
        raise TypeError("Payload must be list")

    if len(payload) > max_size:
        raise OverflowError(f"Payload size must not be greater than max_size {max_size}")


payload = [1, 2, 3, 4, 5]
max_size = 3
ingest_payload(payload=payload, max_size=max_size)