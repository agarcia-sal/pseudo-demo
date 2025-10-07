from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    if not list_of_numbers:
        raise ValueError("list_of_numbers must not be empty")
    mean: float = sum(list_of_numbers) / len(list_of_numbers)
    total_absolute_difference: float = 0.0
    for number in list_of_numbers:
        total_absolute_difference += abs(number - mean)
    mad: float = total_absolute_difference / len(list_of_numbers)
    return mad