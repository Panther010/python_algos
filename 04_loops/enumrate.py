"""
Scenario: 
You are parsing a multi-gigabyte log file loaded into memory as a list of strings. 
When an "ERROR" occurs, you need to log both the 1-based line number and the error message for debugging.
"""

def find_error_lines(logs: list[str]) -> list[tuple[int, str]]:
    result = []
    for line_num, log in enumerate(logs, start=1):
        if 'ERROR' in log:
            result.append((line_num, log))
    return result

log_stream = [
    "INFO: Job started",
    "DEBUG: Connecting to DB",
    "ERROR: Connection timeout on host A",
    "INFO: Retrying connection",
    "ERROR: Max retries exceeded"
]

print(find_error_lines(log_stream))