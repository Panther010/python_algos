"""
Scenario: 
You have a list of user profiles extracted from an analytics database represented as dictionaries.
You need to quickly sort them without writing a full def function.
"""

# Test data
users_list = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 85},
    {"name": "Diana", "score": 95}
]

def sort_users_by_activity_stable(users: list[dict]) -> list[dict]:
    return sorted(users, key=lambda x: (-x["score"], x["name"]))

print(sort_users_by_activity_stable(users_list))