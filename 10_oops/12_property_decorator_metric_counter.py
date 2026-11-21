"""
The Statement: 
Create a class PipelineMetrics with properties for total_processed and total_errors. 
Implement a property error_rate (calculated as errors / processed) 
and a setter or custom threshold hook where setting error_threshold 
triggers a callback function (or sets an internal warning flag is_degraded = True) 
whenever error_rate exceeds error_threshold.
"""
class PipelineMetrics:

    def __init__(self, error_threshold: float):
        self.error_threshold = error_threshold
        self._total_processed = 0
        self._total_errors = 0
        self.is_degraded = False

    @property
    def total_processed(self) -> int:
        return self._total_processed

    @total_processed.setter
    def total_processed(self, val: int):
        if val <= 0:
            raise ValueError("total processed record must be positive")
        self._total_processed = val

    @property
    def total_errors(self) -> int:
        return self._total_errors

    @total_errors.setter
    def total_errors(self, val: int):
        self._total_errors = val

    @property
    def error_rate(self) -> int:
        error_rate =  self.total_errors / self.total_processed
        if error_rate >= self.error_threshold:
            self.is_degraded = True

        return error_rate


if __name__ == "__main__":
    metrics = PipelineMetrics(error_threshold=0.05) # 5% threshold
    metrics.total_processed = 100
    metrics.total_errors = 6 # 6% error rate
    print(metrics.error_rate)
    print(metrics.is_degraded)