"""
The Problem Statement: 
Create a class named PipelineConfig. 
Its constructor (__init__) should accept three parameters: 
    source_path (str), destination_table (str), and batch_size (int, defaulting to 1000). 
Add a method named summary(self) that returns a formatted dictionary containing 
    all configuration attributes.
"""

class PipelineConfig:

    def __init__(self, source_path: str, destination_table: str, batch_size: int = 1000) -> None:
        self.source_path = source_path
        self.destination_table = destination_table
        self.batch_size = batch_size

    def summary(self) -> dict:
        return {
            "source": self.source_path,
            "destination": self.destination_table,
            "batch": self.batch_size
        }


if __name__ == "__main__":
    conf = PipelineConfig(source_path="s3://bucket/raw/logs/", destination_table="analytics.user_logs", batch_size=5000)
    print(conf.summary())