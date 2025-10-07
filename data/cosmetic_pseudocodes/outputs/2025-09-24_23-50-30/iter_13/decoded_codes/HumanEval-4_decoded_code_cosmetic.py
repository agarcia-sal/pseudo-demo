from typing import Sequence

def mean_absolute_deviation(sequence: Sequence[float]) -> float:
    count: int = len(sequence)
    if count == 0:
        return 0.0  # Handle empty sequence gracefully

    average: float = sum(sequence) / count
    deviations = [(element - average) if element > average else (average - element) for element in sequence]
    sum_dev: float = sum(deviations)
    return sum_dev / count