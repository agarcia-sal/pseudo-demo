from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count: int = len(list_of_numbers)
    if count == 0:
        raise ValueError("list_of_numbers must not be empty")
    sum_numbers: float = 0.0
    idx: int = 0
    while idx < count:
        sum_numbers += list_of_numbers[idx]
        idx += 1
    average: float = sum_numbers / count

    sum_dev: float = 0.0
    for element in list_of_numbers:
        diff: float = element - average
        diff_pos: float = diff if diff >= 0 else -diff
        sum_dev += diff_pos

    return sum_dev / count