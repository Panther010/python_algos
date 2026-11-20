"""
The Statement: 
Create a class WarehouseConnection with a standard constructor __init__(self, host, port) 
and a class method from_env(cls, env_dict: dict) 
that reads "DB_HOST" and "DB_PORT" from the dictionary and returns an instance of the class.
"""
class WarehouseConnection:

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    @classmethod
    def from_env(cls, env_dict) -> str:
        return cls(
            host=env_dict["DB_HOST"],
            port=env_dict["DB_PORT"]
        )


if __name__ == "__main__":
    env = {"DB_HOST": "warehouse.internal", "DB_PORT": "5432"}
    conn = WarehouseConnection.from_env(env)
    print(conn.port, conn.host)