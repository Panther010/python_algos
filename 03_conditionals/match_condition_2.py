pipeline_events = [
    {"type": "ingestion", "source": "s3", "status": "success", "rows": 15000},
    {"type": "ingestion", "source": "kafka", "status": "failed", "error": "connection_timeout"},
    {"type": "transformation", "job": "clean_users", "status": "success", "duration_sec": 45},
    {"type": "transformation", "job": "aggregate_sales", "status": "failed", "error": "oom_exception", "duration_sec": 320},
    {"type": "export", "destination": "snowflake", "status": "success", "rows": 15000},
    {"type": "alert", "severity": "critical", "message": "Storage capacity > 90%"},
    {"type": "unknown_payload", "data": [1, 2, 3]}
]

def process_event(event:dict) -> str:
    result = ''
    match event:
        case {'type': 'ingestion', 'status': 'success'}:
            result = f"Ingested {event['rows']} rows from source: {event['source']}"
        case {'type': 'ingestion', 'status': 'failed'}:
            result = f"Ingestion failed from {event['source']} due to: {event['error']}"
        case {'type': 'transformation', 'status': 'success'}:
            if event['duration_sec'] > 60:
                result = f"Warning: Job {event['job']} took a long time ({event['duration_sec']}s)"
            else:
                result = f"Job {event['job']} completed successfully"
        case {'type': 'transformation', 'status': 'failed'}:
            result = f"Job {event['job']} failed with error: {event['error']}"
        case {'type': 'export', 'status': 'success'}:
                result = f"Exported {event['rows']} rows to destination: {event['destination']}"
        case {'type': 'alert'}:
                result = f"CRITICAL ALERT: {event['message']}"
        case _:
              result = f"Unhandled event format: {event}"
    return result

def process_event2(event: dict) -> str:
    match event:
        # 1. Successful Ingestion (Binding variables directly) push validation
        case {"type": "ingestion", "status": "success", "rows": rows, "source": source}:
            return f"Ingested {rows} rows from source: {source}"
            
        # 2. Failed Ingestion
        case {"type": "ingestion", "status": "failed", "source": source, "error": error}:
            return f"Ingestion failed from {source} due to: {error}"
            
        # 3 & 4. Transformations with a Guard Clause
        case {"type": "transformation", "status": "success", "job": job, "duration_sec": duration} if duration > 60:
            return f"Warning: Job {job} took a long time ({duration}s)"
            
        case {"type": "transformation", "status": "success", "job": job}:
            return f"Job {job} completed successfully"
            
        # 5. Transformation Failure
        case {"type": "transformation", "status": "failed", "job": job, "error": error}:
            return f"Job {job} failed with error: {error}"
            
        # 6. Export Success
        case {"type": "export", "status": "success", "rows": rows, "destination": destination}:
            return f"Exported {rows} rows to destination: {destination}"
            
        # 7. Critical Alerts
        case {"type": "alert", "severity": "critical", "message": message}:
            return f"CRITICAL ALERT: {message}"
            
        # 8. Wildcard / Catch-all
        case _:
            return f"Unhandled event format: {event}"

for ev in pipeline_events:
    print(process_event(ev))