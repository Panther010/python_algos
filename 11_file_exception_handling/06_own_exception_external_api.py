"""
The Statement: 
Write a function check_api_response(status_code: int, headers: dict) 
that inspects the HTTP status code. 
If status_code == 429, 
raise a ConnectionError whose message includes the retry seconds specified in headers.
get("Retry-After", 60). 
If status_code >= 500, raise a TimeoutError. Otherwise, return True.
"""
def check_api_response(status_code: int, headers: dict) -> bool:
    if status_code == 429:
        retry_after = headers.get("Retry-After", 60)
        raise ConnectionError(f"Rate limited {(status_code)}. Retry after {retry_after} seconds.")
    elif status_code >= 500:
        raise TimeoutError
    else:
        return True


status = 429
headers = {"Retry-After": "120"}
print(check_api_response(status, headers))