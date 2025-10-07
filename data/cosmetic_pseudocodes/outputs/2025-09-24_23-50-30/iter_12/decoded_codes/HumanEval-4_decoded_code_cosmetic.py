from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count: int = len(list_of_numbers)
    if count == 0:
        return 0.0  # handle empty list to avoid division by zero
    avg: float = sum(list_of_numbers) / count
    deviations: List[float] = [abs(list_of_numbers[i] - avg) for i in range(count)]
    total_dev: float = 0.0
    i: int = 0
    while i < len(deviations):
        total_dev += deviations[i]
        i += 1
    return total_dev / count