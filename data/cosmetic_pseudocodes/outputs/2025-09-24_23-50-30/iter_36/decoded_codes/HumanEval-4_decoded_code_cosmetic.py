from typing import Sequence

def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    aggregate_sum: float = 0.0
    count_elements: int = 0

    for element in sequence_of_values:
        aggregate_sum += element
        count_elements += 1

    if count_elements == 0:
        raise ValueError("mean_absolute_deviation() arg is an empty sequence")

    average: float = aggregate_sum / count_elements

    cumulative_deviation: float = 0.0
    index_counter: int = 0

    while index_counter < count_elements:
        current_deviation = sequence_of_values[index_counter] - average
        absolute_deviation = -current_deviation if current_deviation < 0 else current_deviation
        cumulative_deviation += absolute_deviation
        index_counter += 1

    result: float = cumulative_deviation / count_elements

    return result