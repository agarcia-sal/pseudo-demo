from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    total_absolute_deviation = 0.0
    for x in numbers:
        difference = x - mean
        if difference < 0:
            absolute_difference = difference * -1
        else:
            absolute_difference = difference
        total_absolute_deviation += absolute_difference
    result = total_absolute_deviation / len(numbers)
    return result