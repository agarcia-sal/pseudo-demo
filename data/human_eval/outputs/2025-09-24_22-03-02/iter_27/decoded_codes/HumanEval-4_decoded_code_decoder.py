from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    total_sum = 0.0
    total_length = 0

    for index in range(len(numbers)):
        total_sum += numbers[index]
        total_length += 1

    mean = total_sum / total_length

    absolute_differences_sum = 0.0

    for index in range(len(numbers)):
        difference = numbers[index] - mean
        if difference < 0:
            absolute_difference = difference * -1
        else:
            absolute_difference = difference
        absolute_differences_sum += absolute_difference

    mad = absolute_differences_sum / total_length

    return mad