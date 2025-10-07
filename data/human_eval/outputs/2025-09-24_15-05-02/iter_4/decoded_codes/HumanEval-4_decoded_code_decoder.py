from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    total_absolute_deviation = 0.0
    for x in numbers:
        total_absolute_deviation += abs(x - mean)
    return total_absolute_deviation / len(numbers)