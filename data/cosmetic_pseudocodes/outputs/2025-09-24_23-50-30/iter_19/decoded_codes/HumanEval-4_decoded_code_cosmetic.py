from typing import Sequence

def mean_absolute_deviation(values: Sequence[float]) -> float:
    n: int = len(values)
    if n == 0:
        raise ValueError("mean_absolute_deviation() arg is an empty sequence")
    average: float = sum(values) / n
    deviations: list[float] = []
    for i in range(n):
        diff: float = values[i] - average
        dev: float = diff if diff > 0 else -diff
        deviations.append(dev)
    total_dev: float = 0.0
    for x in deviations:
        total_dev += x
    return total_dev / n