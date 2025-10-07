from typing import List


def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count: int = len(list_of_numbers)
    if count == 0:
        raise ValueError("list_of_numbers must not be empty")
    sum_numbers: float = 0.0
    for number in list_of_numbers:
        sum_numbers += number
    mean_value: float = sum_numbers / count

    deviation_sum: float = 0.0
    for number in list_of_numbers:
        deviation_sum += abs(number - mean_value)

    mean_absolute_deviation_value: float = deviation_sum / count
    return mean_absolute_deviation_value