from typing import List, Union

def mean_absolute_deviation(list_of_numbers: List[Union[int, float]]) -> float:
    if not list_of_numbers:
        raise ValueError("Input list must not be empty")
    length: int = len(list_of_numbers)
    mean_value: float = sum(list_of_numbers) / length
    total_absolute_deviation: float = 0.0
    for number in list_of_numbers:
        total_absolute_deviation += abs(number - mean_value)
    mean_absolute_deviation: float = total_absolute_deviation / length
    return mean_absolute_deviation