from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    total_sum = 0.0
    count = 0
    for index in range(len(numbers)):
        total_sum += numbers[index]
        count += 1
    mean = total_sum / count
    absolute_difference_sum = 0.0
    for index in range(len(numbers)):
        difference = numbers[index] - mean
        if difference < 0:
            difference = -difference
        absolute_difference_sum += difference
    result = absolute_difference_sum / count
    return result