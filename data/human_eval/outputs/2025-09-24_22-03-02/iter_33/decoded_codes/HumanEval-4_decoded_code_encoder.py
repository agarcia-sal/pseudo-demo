from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    total_sum = 0.0
    number_of_elements = len(numbers)
    index = 0
    while index < number_of_elements:
        total_sum += numbers[index]
        index += 1
    mean = total_sum / number_of_elements
    total_absolute_deviation = 0.0
    index = 0
    while index < number_of_elements:
        current_value = numbers[index]
        difference = current_value - mean
        if difference < 0.0:
            difference *= -1.0
        total_absolute_deviation += difference
        index += 1
    mean_absolute_deviation_result = total_absolute_deviation / number_of_elements
    return mean_absolute_deviation_result