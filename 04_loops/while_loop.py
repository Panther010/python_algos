"""
Scenario: 
Your pipeline triggers an external cloud data warehouse sync job via an API. 
The job runs asynchronously, and you must poll its status in a loop until it returns "SUCCESS"
 or "FAILED".
"""

# Test data (simulating consecutive API responses over time)
simulated_api_responses = ["PENDING", "PENDING", "RUNNING", "RUNNING", "SUCCESS"]

def poll_job_status(status_sequence: list[str]):
    counter = 0
    while status_sequence:
        current_request = status_sequence.pop(0)
        counter += 1

        if current_request == "SUCCESS" or current_request == "FAILED":
            return f"JOB completed after {counter} attemps with status: {current_request}"

    return "Polling finished, JOB is yet to complete"

print(poll_job_status(simulated_api_responses))