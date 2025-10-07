from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    total_absolute_difference = 0
    for x in numbers:
        absolute_difference = abs(x - mean)
        total_absolute_difference += absolute_difference
    mad = total_absolute_difference / len(numbers)
    return mad