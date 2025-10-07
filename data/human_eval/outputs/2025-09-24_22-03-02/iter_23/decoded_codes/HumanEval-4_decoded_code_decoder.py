from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = 0.0
    total_sum = 0.0
    count = 0
    absolute_difference_sum = 0.0

    for index in range(len(numbers)):
        total_sum += numbers[index]
        count += 1

    mean = total_sum / count

    for index in range(len(numbers)):
        difference = numbers[index] - mean
        if difference < 0.0:
            difference = 0.0 - difference
        absolute_difference_sum += difference

    return absolute_difference_sum / count