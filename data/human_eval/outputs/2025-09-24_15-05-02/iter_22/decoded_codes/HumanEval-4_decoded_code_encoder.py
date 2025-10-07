from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    if not list_of_numbers:
        raise ValueError("list_of_numbers must not be empty")
    mean_value: float = sum(list_of_numbers) / len(list_of_numbers)
    total_absolute_deviation: float = 0.0
    for number in list_of_numbers:
        total_absolute_deviation += abs(number - mean_value)
    mean_absolute_deviation_value: float = total_absolute_deviation / len(list_of_numbers)
    return mean_absolute_deviation_value