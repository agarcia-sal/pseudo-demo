from typing import Sequence

def mean_absolute_deviation(collection_of_values: Sequence[float]) -> float:
    count_values = len(collection_of_values)
    accumulator_sum = 0.0
    idx = 0
    while idx < count_values:
        accumulator_sum += collection_of_values[idx]
        idx += 1
    average_value = accumulator_sum / count_values if count_values > 0 else 0.0

    sum_distance = 0.0
    pointer = 0
    while pointer < count_values:
        difference = collection_of_values[pointer] - average_value
        distance = -difference if difference < 0 else difference
        sum_distance += distance
        pointer += 1

    result_measure = sum_distance / count_values if count_values > 0 else 0.0
    return result_measure