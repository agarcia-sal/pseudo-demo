from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    mean_value = sum(list_of_numbers) / len(list_of_numbers)
    total_absolute_difference = 0
    for number in list_of_numbers:
        total_absolute_difference += abs(number - mean_value)
    mean_absolute_deviation = total_absolute_difference / len(list_of_numbers)
    return mean_absolute_deviation