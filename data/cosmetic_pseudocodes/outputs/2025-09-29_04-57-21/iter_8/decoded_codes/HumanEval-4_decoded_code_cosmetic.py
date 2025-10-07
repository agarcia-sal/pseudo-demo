from typing import Sequence


def mean_absolute_deviation(list_of_numbers: Sequence[float]) -> float:
    count: int = 0
    sum_accumulator: float = 0.0
    length = len(list_of_numbers)
    if length == 0:
        # Avoid division by zero; MAD is undefined for empty input, decide to return 0.0
        return 0.0

    while count < length:
        sum_accumulator += list_of_numbers[count]
        count += 1

    average = sum_accumulator * (1 / length)

    distance_accumulator: float = 0.0
    index: int = 0
    while True:
        subtraction_result = list_of_numbers[index] - average
        positive_diff = subtraction_result if subtraction_result >= 0 else -subtraction_result

        distance_accumulator += positive_diff
        index += 1
        if not (index < length):
            break

    mad_result = distance_accumulator * (1 / length)
    return mad_result