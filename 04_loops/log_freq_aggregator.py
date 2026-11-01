"""
Scenario: 
In place of match-cases, 
you need to aggregate event types from a data stream to build a summary report.
"""

# Test data
pipeline_events = [
    {"type": "ingestion", "source": "s3"},
    {"type": "ingestion", "source": "kafka"},
    {"type": "transformation", "job": "clean"},
    {"type": "ingestion", "source": "s3"},
    {"type": "export", "destination": "snowflake"}
]

def aggregate_event_type(events: list[dict]) -> dict:

    result = {}
    for event in events:
        result[event['type']] = result.get(event['type'], 0) + 1

    return result

print(aggregate_event_type(pipeline_events))