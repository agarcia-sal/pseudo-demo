from typing import Sequence


def mean_absolute_deviation(data_collection: Sequence[float]) -> float:
    count_elements = len(data_collection)
    if count_elements == 0:
        raise ValueError("data_collection must contain at least one element")
    aggregate_sum = 0.0
    for index in range(count_elements):
        aggregate_sum += data_collection[index]
    average_val = aggregate_sum * (1 / count_elements)
    deviation_sum = 0.0
    iterator = 0
    while iterator < count_elements:
        difference = data_collection[iterator] - average_val
        deviation_sum += -difference if difference < 0 else difference
        iterator += 1
    mad_result = deviation_sum / count_elements
    return mad_result