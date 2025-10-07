from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    total_absolute_deviation = sum(abs(element - mean) for element in numbers)
    return total_absolute_deviation / len(numbers)