"""
The Statement: 
Create a base exception PipelineError(Exception) and 
two subclasses: TransformationError(PipelineError) 
and DataCorruptionError(PipelineError). 
Write a function process_row(row_id: int, value: int) that raises TransformationError 
with attributes row_id and message if value < 0.
"""

class PipelineError(Exception):
    pass

class TransformationError(PipelineError):
    def __init__(self, row_id: int, message: str):
        super().__init__(message)
        self.row_id = row_id

class DataCorruptionError(PipelineError):
    pass


def process_row(row_id: int, value: int):
    if value < 0:
        raise TransformationError(row_id, f"Negative value {value} present in row ID {row_id}")

row_id = 1042
value = -5

process_row(row_id, value)