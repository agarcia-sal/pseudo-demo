from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count: int = len(list_of_numbers)
    if count == 0:
        return 0.0
    mean_val: float = 0.0
    sum_abs_dev: float = 0.0

    for i in range(count):
        mean_val += list_of_numbers[i]
    mean_val /= count

    for index in range(count):
        sum_abs_dev += abs(list_of_numbers[index] - mean_val)

    return sum_abs_dev / count