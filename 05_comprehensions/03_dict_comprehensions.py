"""
Context: 
Joining streaming facts against dimension tables often 
requires building O(1) in-memory lookup indices on the fly.

The Problem: 
Write a function build_partition_index(metadata_list: list[dict]) -> dict
using a dict comprehension. 
Take a list of partition records and map each partition's path directly to 
its owner_team, but only include partitions where is_active is True.
"""

# Test Data
partition_metadata = [
    {"path": "s3://lake/ds=2026-06-01", "owner_team": "analytics", "is_active": True},
    {"path": "s3://lake/ds=2026-05-15", "owner_team": "growth", "is_active": False},
    {"path": "s3://lake/ds=2026-06-02", "owner_team": "core_eng", "is_active": True}
]

def build_partition_index(metadata_list: list[dict]) -> dict:
    return { x['path'] : x['owner_team']
        for x in metadata_list
        if x['is_active'] == True
    }
    
print(build_partition_index(partition_metadata))