from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    if not list_of_numbers:
        return 0.0
    mean_value = sum(list_of_numbers) / len(list_of_numbers)
    total_absolute_deviation = sum(abs(x - mean_value) for x in list_of_numbers)
    mean_absolute_deviation_value = total_absolute_deviation / len(list_of_numbers)
    return mean_absolute_deviation_value