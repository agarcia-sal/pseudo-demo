from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    n = len(list_of_numbers)
    if n == 0:
        raise ValueError("list_of_numbers must not be empty")
    mean_value = sum(list_of_numbers) / n
    total_absolute_deviation: float = 0
    for number in list_of_numbers:
        total_absolute_deviation += abs(number - mean_value)
    mean_absolute_deviation_value = total_absolute_deviation / n
    return mean_absolute_deviation_value