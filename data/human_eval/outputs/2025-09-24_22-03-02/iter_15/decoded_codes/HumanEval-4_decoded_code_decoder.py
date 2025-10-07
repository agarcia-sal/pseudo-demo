from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    total_absolute_deviation = 0.0
    for x in numbers:
        absolute_difference = abs(x - mean)
        total_absolute_deviation += absolute_difference
    mad = total_absolute_deviation / len(numbers)
    return mad