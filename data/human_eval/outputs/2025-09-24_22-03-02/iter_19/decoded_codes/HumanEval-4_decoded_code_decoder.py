from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    sum_of_numbers = 0.0
    length_of_numbers = len(numbers)
    index = 0
    while index < length_of_numbers:
        sum_of_numbers += numbers[index]
        index += 1
    mean = sum_of_numbers / length_of_numbers
    sum_of_absolute_differences = 0.0
    index = 0
    while index < length_of_numbers:
        difference = numbers[index] - mean
        if difference < 0.0:
            absolute_difference = -difference
        else:
            absolute_difference = difference
        sum_of_absolute_differences += absolute_difference
        index += 1
    mean_absolute_deviation = sum_of_absolute_differences / length_of_numbers
    return mean_absolute_deviation