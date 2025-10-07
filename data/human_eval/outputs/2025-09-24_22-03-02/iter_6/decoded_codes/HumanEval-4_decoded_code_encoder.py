from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    total_deviation = sum(abs(number - mean) for number in numbers)
    return total_deviation / len(numbers)