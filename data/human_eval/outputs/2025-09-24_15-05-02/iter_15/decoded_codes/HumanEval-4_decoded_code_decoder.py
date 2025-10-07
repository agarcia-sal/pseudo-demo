from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    total_absolute_difference = 0
    for element in numbers:
        total_absolute_difference += abs(element - mean)
    mean_absolute_deviation = total_absolute_difference / len(numbers)
    return mean_absolute_deviation