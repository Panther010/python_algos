"""
Context: 
    Senior and Lead interviews frequently grill you on memory complexity ($O(1)$ space). 
    Processing a 50GB file requires generators instead of loading everything into a list comprehension.
need to work on generator
Write a generator function or generator expression pipeline called stream_cleaned_logs(log_stream).
It should take an iterable stream of raw log strings.
Using a generator expression, it filters out lines starting with "DEBUG:" and strips whitespace.
Then, write a wrapper function batch_generator(iterable, batch_size: int) that yields chunks (batches) of size batch_size from that stream.
"""
raw_log_generator = iter([
    "INFO: Start job",
    "DEBUG: Internal state X",
    "ERROR: DB timeout",
    "INFO: Retrying query",
    "WARN: High memory usage",
    "ERROR: Out of memory"
])