from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    if not list_of_numbers:
        raise ValueError("Input list must not be empty")
    length: int = len(list_of_numbers)
    mean_value: float = sum(list_of_numbers) / length
    total_absolute_deviation: float = sum(abs(number - mean_value) for number in list_of_numbers)
    mean_absolute_deviation: float = total_absolute_deviation / length
    return mean_absolute_deviation