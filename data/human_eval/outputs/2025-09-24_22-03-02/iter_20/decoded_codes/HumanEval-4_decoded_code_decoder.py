from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Input list must not be empty")
    sum_numbers = 0.0
    length_numbers = 0
    for index in range(len(numbers)):
        sum_numbers += numbers[index]
        length_numbers += 1
    mean = sum_numbers / length_numbers
    sum_absolute_differences = 0.0
    for index in range(len(numbers)):
        difference = numbers[index] - mean
        if difference < 0.0:
            absolute_difference = -difference
        else:
            absolute_difference = difference
        sum_absolute_differences += absolute_difference
    mad = sum_absolute_differences / length_numbers
    return mad