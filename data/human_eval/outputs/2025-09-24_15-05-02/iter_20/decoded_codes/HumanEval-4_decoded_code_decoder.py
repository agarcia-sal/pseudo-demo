from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    n = len(list_of_numbers)
    if n == 0:
        raise ValueError("list_of_numbers must not be empty")
    mean_value = sum(list_of_numbers) / n
    total_deviation = sum(abs(number - mean_value) for number in list_of_numbers)
    mean_absolute_deviation = total_deviation / n
    return mean_absolute_deviation