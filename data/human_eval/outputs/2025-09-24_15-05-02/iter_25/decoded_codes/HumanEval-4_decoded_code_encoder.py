from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    if not list_of_numbers:
        return 0.0
    mean: float = sum(list_of_numbers) / len(list_of_numbers)
    total_absolute_difference: float = sum(abs(number - mean) for number in list_of_numbers)
    mad: float = total_absolute_difference / len(list_of_numbers)
    return mad