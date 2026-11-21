"""
The Statement: 
Create a class DataFrameWrapper initialized with a raw list of dictionaries. 
Implement a read-only @property columns that returns sorted unique keys, 
and a read-only @property row_count that computes the number of rows dynamically. 
Also include a setter for the raw data that validates that every row is a dictionary.
"""
class DataFrameWrapper:

    def __init__(self, rows: list) -> None:
        self._rows = rows

    @property
    def rows(self) -> list:
        return self._rows

    @rows.setter
    def rows(self, rows:list):
        for row in rows:
            if not isinstance(row, dict):
                raise ValueError("Every row must be a dictionary")          
        self._rows = rows

    @property
    def columns(self) -> list:
        return sorted(list({col for row in self._rows for col in row.keys()}))


    @property
    def row_count(self) -> int:
        return len(self._rows)


if __name__ == "__main__":
    df = DataFrameWrapper([{"id": 1, "val": 10}, {"id": 2, "val": 20}])
    df.columns == ["id", "val"]
    df.row_count == 2
    print(df.columns)
    print(df.row_count)