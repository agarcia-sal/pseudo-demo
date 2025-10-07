from typing import Sequence

def mean_absolute_deviation(numbers: Sequence[float]) -> float:
    if not numbers:
        raise ValueError("numbers must not be empty")
    total_sum = 0.0
    total_count = 0
    index = 0
    while index < len(numbers):
        current_element = numbers[index]
        total_sum += current_element
        index += 1
    mean = total_sum / len(numbers)
    total_absolute_deviation_sum = 0.0
    index = 0
    while index < len(numbers):
        current_element = numbers[index]
        difference = current_element - mean
        if difference < 0:
            absolute_difference = 0 - difference
        else:
            absolute_difference = difference
        total_absolute_deviation_sum += absolute_difference
        index += 1
    mad = total_absolute_deviation_sum / len(numbers)
    return mad