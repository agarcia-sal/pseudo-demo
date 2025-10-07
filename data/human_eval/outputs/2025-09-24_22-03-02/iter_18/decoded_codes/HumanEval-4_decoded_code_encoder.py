from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    total_sum = 0.0
    length = 0
    for index in range(len(numbers)):
        total_sum += numbers[index]
        length += 1
    mean = total_sum / length
    absolute_difference_sum = 0.0
    for index in range(length):
        element = numbers[index]
        if element >= mean:
            difference = element - mean
        else:
            difference = mean - element
        absolute_difference_sum += difference
    mad = absolute_difference_sum / length
    return mad