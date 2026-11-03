"""
Context: 
Schema drift happens when upstream databases introduce or drop columns across different shards or regions. 
You need to identify missing columns instantly.
"""

# Test Data
standard_schema = {"user_id", "event_timestamp", "payload", "country"}
region_data_shards = [
    {"region": "us", "columns": {"user_id", "event_timestamp", "payload", "country", "legacy_col"}},
    {"region": "ap", "columns": {"user_id", "event_timestamp", "payload"}} # missing 'country' and has drift
]

def find_drifted_columns(global_standards: set[str], region_schemas:list[dict]) -> set[str]:
    return {col
              for x in region_schemas
              for col in (x['columns'] ^ global_standards)}

print(find_drifted_columns(standard_schema, region_data_shards))