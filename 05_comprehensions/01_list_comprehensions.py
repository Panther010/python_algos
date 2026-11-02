"""
Context: 
Pipelines frequently ingest nested JSON or JSONL payloads where arrays of metrics are embedded inside partition records. 
You need to extract and filter these efficiently in a single readable pass.
"""

# Test Data
cluster_telemetry = [
    {
        "region": "us-east-1",
        "nodes": [
            {"node_id": "node-101", "status": "active", "cpu_utilization": 88.5},
            {"node_id": "node-102", "status": "maintenance", "cpu_utilization": 95.0}
        ]
    },
    {
        "region": "eu-west-1",
        "nodes": [
            {"node_id": "node-201", "status": "active", "cpu_utilization": 91.2},
            {"node_id": "node-202", "status": "active", "cpu_utilization": 45.0}
        ]
    }
]

def extract_high_cpu_metrics(partitions: list[dict], threshold: float) -> list[dict]:
    return [{'node_id': y['node_id'], "cpu": y["cpu_utilization"]} 
            for x in partitions 
            for y in x['nodes'] 
            if y['status'] == 'active' and y['cpu_utilization'] > threshold]

for i in extract_high_cpu_metrics(cluster_telemetry, 80.0):
    print(i)