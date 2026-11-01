"""
Scenario: 
You are searching through a prioritized list of cloud storage bucket paths to find 
an available data partition. If you find one, you process it and exit. 
If you loop through all paths and find none of them exist, 
you must trigger a default fallback mechanism.
"""

# Test data
all_paths = ["s3://bucket/date=2026-06-01", "s3://bucket/date=2026-06-02", "s3://bucket/date=2026-06-03"]
active_buckets = {"s3://bucket/date=2026-06-02", "s3://bucket/date=2026-06-03"}


def find_active_partition(partitions: list[str], available_set: set[str]) -> str:
    for partition in partitions:
        print(f"Checking partition {partition}")
        if partition in available_set:
            return f"Found partition: {partition}"

    else:
        return f"No partition availale, using default storage"

print(find_active_partition(all_paths, active_buckets))