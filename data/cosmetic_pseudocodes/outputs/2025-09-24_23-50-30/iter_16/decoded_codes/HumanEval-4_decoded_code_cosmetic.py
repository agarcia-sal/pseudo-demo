from typing import Sequence

def mean_absolute_deviation(sequence_of_elements: Sequence[float]) -> float:
    count_elements: int = len(sequence_of_elements)
    if count_elements == 0:
        raise ValueError("mean_absolute_deviation() arg is an empty sequence")

    aggregate_sum: float = 0.0
    for index in range(count_elements):
        aggregate_sum += sequence_of_elements[index]
    average_value: float = aggregate_sum / count_elements

    deviations_collection: list[float] = []
    pointer: int = 0
    while pointer < count_elements:
        difference: float = sequence_of_elements[pointer] - average_value
        positive_diff: float = difference if difference >= 0 else -difference
        deviations_collection.append(positive_diff)
        pointer += 1

    total_dev: float = 0.0
    for value in deviations_collection:
        total_dev += value
    final_result: float = total_dev / count_elements

    return final_result