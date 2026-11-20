"""
The Statement: 
Create a class JobConfig with a private attribute _timeout_seconds.
Use @property and @timeout_seconds.setter to ensure 
that any attempt to assign a negative value raises a ValueError.
"""

class JobConfig:

    def __init__(self, timeout_seconds) -> None:
        self._timeout_seconds = timeout_seconds

    @property
    def timeout_seconds(self) -> int:
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        if timeout_seconds <= 0:
            raise ValueError("Timeout value must be positive")
        else:
            self._timeout_seconds = timeout_seconds


if __name__ == "__main__":
    config = JobConfig(timeout_seconds=300)
    print(config.timeout_seconds)
    config.timeout_seconds = 600
    print(config.timeout_seconds == 600)
