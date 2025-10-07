from typing import Sequence, Union

def mean_absolute_deviation(list_of_numbers: Sequence[Union[int, float]]) -> float:
    n = len(list_of_numbers)
    if n == 0:
        raise ValueError("mean_absolute_deviation() arg is an empty sequence")
    mean_value = sum(list_of_numbers) / n
    total_absolute_difference = sum(abs(x - mean_value) for x in list_of_numbers)
    return total_absolute_difference / n