from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    n: int = len(list_of_numbers)
    if n == 0:
        return 0.0
    mean_value: float = sum(list_of_numbers) / n

    sum_abs_diff: float = sum(abs(num - mean_value) for num in list_of_numbers)
    result: float = sum_abs_diff / n
    return result