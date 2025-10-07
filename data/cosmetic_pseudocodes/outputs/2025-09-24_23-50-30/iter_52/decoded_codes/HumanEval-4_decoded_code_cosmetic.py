from typing import Sequence


def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    def compute_sum(collection: Sequence[float], accumulator: float, index: int) -> float:
        if index >= len(collection):
            return accumulator
        return compute_sum(collection, accumulator + collection[index], index + 1)

    def compute_abs_sum_diff(collection: Sequence[float], pivot: float, accumulator: float, index: int) -> float:
        if index >= len(collection):
            return accumulator
        temp_diff = collection[index] - pivot
        abs_diff = temp_diff if temp_diff >= 0 else -temp_diff
        return compute_abs_sum_diff(collection, pivot, accumulator + abs_diff, index + 1)

    total_elements = len(sequence_of_values)
    if total_elements == 0:
        raise ValueError("sequence_of_values must not be empty")
    accumulated_sum = compute_sum(sequence_of_values, 0.0, 0)
    central_value = accumulated_sum / total_elements
    total_deviation = compute_abs_sum_diff(sequence_of_values, central_value, 0.0, 0)
    final_result = total_deviation / total_elements
    return final_result