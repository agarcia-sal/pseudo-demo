from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count = len(list_of_numbers)
    if count == 0:
        raise ValueError("list_of_numbers must not be empty")
    average = sum(list_of_numbers) / count
    deviations = [abs(number - average) for number in list_of_numbers]
    mad = sum(deviations) / count
    return mad