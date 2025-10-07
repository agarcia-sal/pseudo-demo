from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    total_sum = 0.0
    count = len(numbers)
    for index in range(count):
        total_sum += numbers[index]
    mean = total_sum / count
    absolute_differences_sum = 0.0
    for index in range(count):
        difference = numbers[index] - mean
        if difference < 0.0:
            difference = -difference
        absolute_differences_sum += difference
    mean_absolute_deviation = absolute_differences_sum / count
    return mean_absolute_deviation