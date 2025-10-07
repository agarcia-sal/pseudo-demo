from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count: int = len(list_of_numbers)
    if count == 0:
        raise ValueError("list_of_numbers must not be empty")

    accumulator: float = 0.0
    pointer: int = 0

    while pointer < count:
        accumulator += list_of_numbers[pointer]
        pointer += 1

    average: float = accumulator / count

    sum_differences: float = 0.0
    index: int = 0

    while index < count:
        difference: float = list_of_numbers[index] - average
        abs_difference: float = difference if difference >= 0 else -difference
        sum_differences += abs_difference
        index += 1

    final_result: float = sum_differences / count
    return final_result