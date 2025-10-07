from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    sum_of_numbers = 0.0
    length_of_numbers = 0
    for index in range(len(numbers)):
        sum_of_numbers += numbers[index]
        length_of_numbers += 1
    mean = sum_of_numbers / length_of_numbers
    sum_of_absolute_differences = 0.0
    for index in range(length_of_numbers):
        difference = numbers[index] - mean
        if difference < 0.0:
            absolute_difference = 0.0 - difference
        else:
            absolute_difference = difference
        sum_of_absolute_differences += absolute_difference
    mean_absolute_deviation = sum_of_absolute_differences / length_of_numbers
    return mean_absolute_deviation