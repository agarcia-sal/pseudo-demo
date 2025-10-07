from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    sum_of_numbers = 0.0
    count_of_numbers = 0
    for index in range(len(numbers)):
        sum_of_numbers += numbers[index]
        count_of_numbers += 1
    if count_of_numbers == 0:
        raise ValueError("Input list must contain at least one number")
    mean = sum_of_numbers / count_of_numbers
    sum_of_absolute_differences = 0.0
    for index in range(len(numbers)):
        difference = numbers[index] - mean
        if difference < 0.0:
            absolute_difference = -difference
        else:
            absolute_difference = difference
        sum_of_absolute_differences += absolute_difference
    mean_absolute_deviation = sum_of_absolute_differences / count_of_numbers
    return mean_absolute_deviation