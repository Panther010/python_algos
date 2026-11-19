"""
The Statement: 
Implement a class DeduplicationEngine 
with a static method generate_token(payload: dict, keys_to_hash: list) -> str 
that extracts specific key-values from a dictionary, 
sorts them canonically to ensure determinism regardless of dictionary key insertion order,
and returns an MD5 hexadecimal digest string.
"""
import json
import hashlib

class DeduplicationEngine:

    @staticmethod
    def generate_token(payload: dict, keys_to_hash: list) -> str:
        required_payload = {key: payload[key] for key in sorted(keys_to_hash) if key in payload}

        str_payload = json.dumps(required_payload, sort_keys=True, separators=(",", ":"))

        return hashlib.md5(str_payload.encode("utf-8")).hexdigest()


if __name__ == "__main__":

    payload_1 = {"b": 2, "a": 1, "c": 3}
    payload_2 = {"a": 1, "c": 3, "b": 2}
    keys = ["a", "b"]

    isinstance(DeduplicationEngine.generate_token(payload_1, keys), str)
    DeduplicationEngine.generate_token(payload_1, keys) == DeduplicationEngine.generate_token(payload_2, keys)