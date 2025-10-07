from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    n = len(list_of_numbers)
    if n == 0:
        raise ValueError("list_of_numbers must not be empty")
    mean_value: float = sum(list_of_numbers) / n
    total_absolute_deviation: float = sum(abs(element - mean_value) for element in list_of_numbers)
    mean_absolute_deviation_value: float = total_absolute_deviation / n
    return mean_absolute_deviation_value