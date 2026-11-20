"""
The Statement: 
Create a class PartitionedDataset with a class method from_path(cls, uri: str) 
that parses a Hive-style path string, 
extracts partition key-value pairs (e.g., year, month, day), 
and returns a class instance initialized with those partition filters.
"""

class PartitionedDataset:

    def __init__(self, partitions: dict) -> None:
        self.partitions = partitions

    @classmethod
    def from_path(cls, uri: str)-> dict:
        return cls(
            {data.split('=')[0] : data.split('=')[1]
            for data in uri.split('/')
            if "=" in data}
        )


if __name__ == "__main__":
    uri = "s3://my-lake/silver/orders/year=2026/month=03/day=18/part-001.parquet"
    dataset = PartitionedDataset.from_path(uri)
    print(dataset.partitions)
