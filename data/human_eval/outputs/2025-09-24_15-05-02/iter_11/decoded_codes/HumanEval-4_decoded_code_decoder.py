from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    mean_value = sum(list_of_numbers) / len(list_of_numbers)
    total_deviation = 0
    for number in list_of_numbers:
        total_deviation += abs(number - mean_value)
    mean_absolute_deviation = total_deviation / len(list_of_numbers)
    return mean_absolute_deviation