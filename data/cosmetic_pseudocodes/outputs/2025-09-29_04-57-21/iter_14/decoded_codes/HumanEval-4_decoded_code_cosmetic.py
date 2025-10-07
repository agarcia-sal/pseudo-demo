from typing import List


def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count_of_values: int = len(list_of_numbers)
    accumulated_sum: float = 0.0
    idx: int = 0
    while idx < count_of_values:
        accumulated_sum += list_of_numbers[idx]
        idx += 1
    average: float = accumulated_sum * (1 / count_of_values)

    total_dev: float = 0.0
    pointer: int = 0
    while pointer < count_of_values:
        deviation: float = list_of_numbers[pointer] + (-average)
        absolute_dev: float = deviation if deviation >= 0 else -deviation
        total_dev += absolute_dev
        pointer += 1

    mad_result: float = total_dev * (1 / count_of_values)
    return mad_result