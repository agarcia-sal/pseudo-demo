from typing import List, Union

def median(list_of_numbers: List[Union[int, float]]) -> float:
    list_of_numbers = sorted(list_of_numbers)
    n = len(list_of_numbers)
    if n % 2 == 1:
        return float(list_of_numbers[n // 2])
    else:
        return (list_of_numbers[n // 2 - 1] + list_of_numbers[n // 2]) / 2.0