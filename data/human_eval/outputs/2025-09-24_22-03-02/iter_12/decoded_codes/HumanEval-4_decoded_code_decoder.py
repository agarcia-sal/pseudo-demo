from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    total_absolute_difference = 0.0
    for x in numbers:
        difference = x - mean
        absolute_difference = abs(difference)
        total_absolute_difference += absolute_difference
    return total_absolute_difference / len(numbers)