"""
The Statement: 
Write a function process_batch_files(file_paths: list, db_connection) -> dict 
that loops through file paths. 
Wrap file processing in try. 
If a PermissionError or IOError occurs on any file, catch it, 
    log the failed file, and 
    break or continue based on policy. 
Use else to mark files as successfully committed in a tracking dictionary, 
and use finally to ensure db_connection.close() is invoked regardless of success or failure.
Return a status report dictionary.
"""
def process_batch_files(file_paths: list, db_connection) -> dict:
    processed = []
    failed = []
    try:
        pass
    except:
        pass
    else:
        pass
    finally:
        pass
    return 