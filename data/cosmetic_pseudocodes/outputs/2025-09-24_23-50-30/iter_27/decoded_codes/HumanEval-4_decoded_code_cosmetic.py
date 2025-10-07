from typing import Sequence

def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    length = len(sequence_of_values)
    if length == 0:
        raise ValueError("mean_absolute_deviation() arg is an empty sequence")

    aggregate_total = 0.0
    index = 0
    while index < length:
        aggregate_total += sequence_of_values[index]
        index += 1
    central_measure = aggregate_total / length

    deviations_collection = [0.0] * length
    position_marker = 0
    while position_marker < length:
        deviations_collection[position_marker] = abs(sequence_of_values[position_marker] - central_measure)
        position_marker += 1

    sum_of_deviations = 0.0
    counter = 0
    while counter < length:
        sum_of_deviations += deviations_collection[counter]
        counter += 1

    result_value = sum_of_deviations / length
    return result_value