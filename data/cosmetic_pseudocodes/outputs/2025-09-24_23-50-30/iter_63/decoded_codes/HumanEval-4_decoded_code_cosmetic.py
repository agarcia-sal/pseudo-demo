from typing import List


def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count: int = 0
    aggregate: float = 0.0
    iterator: int = 0

    while iterator < len(list_of_numbers):
        aggregate += list_of_numbers[iterator]
        iterator += 1

    count = len(list_of_numbers)
    if count == 0:
        # Avoid division by zero for empty list
        return 0.0

    average: float = aggregate / count

    difference_sum: float = 0.0
    for index in range(count):
        difference_sum += abs(list_of_numbers[index] - average)

    mad_result: float = difference_sum / count

    return mad_result