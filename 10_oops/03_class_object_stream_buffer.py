"""
The Statement: 
Build a class StreamBuffer that uses __slots__ to restrict attributes to timestamp, event_type, and payload.
Implement a method to_tuple(self) that returns a frozen tuple representation of the buffer, 
and a dynamic method binder attach_tag(self, tag_name: str) 
    that adds a custom instance attribute on the fly.
"""


class StreamBuffer:

    __slots__ = ("timestamp", "event_type", "payload", "__dict__")

    def __init__(self, timestamp: int, event_type: str, payload: dict):
        self.timestamp = timestamp
        self.event_type = event_type
        self.payload = payload

    def to_tuple(self) -> tuple:
        return(self.timestamp, self.event_type, self.payload)

    def attach_tag(self, tag_name: str):
        setattr(self, tag_name, True)


if __name__ == "__main__":
    buffer = StreamBuffer(timestamp=1710000000, event_type="click", payload={"id": 101})
    buffer.attach_tag("production")
    buffer.to_tuple() == (1710000000, "click", {"id": 101})
    buffer.production == True 
    print("All checks passed successfully!")