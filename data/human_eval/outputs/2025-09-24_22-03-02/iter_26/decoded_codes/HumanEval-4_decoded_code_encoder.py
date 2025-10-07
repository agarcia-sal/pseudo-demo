from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    sum_of_numbers = 0
    for index in range(len(numbers)):
        number = numbers[index]
        sum_of_numbers += number
    mean = sum_of_numbers / len(numbers)
    sum_of_absolute_differences = 0
    for index in range(len(numbers)):
        number = numbers[index]
        difference = number - mean
        if difference < 0:
            absolute_difference = -difference
        else:
            absolute_difference = difference
        sum_of_absolute_differences += absolute_difference
    mean_absolute_deviation_value = sum_of_absolute_differences / len(numbers)
    return mean_absolute_deviation_value