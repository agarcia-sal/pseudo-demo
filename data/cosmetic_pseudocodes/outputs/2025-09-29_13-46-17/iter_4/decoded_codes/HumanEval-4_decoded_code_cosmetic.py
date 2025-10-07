from typing import Sequence


def mean_absolute_deviation(data_sequence: Sequence[float]) -> float:
    def accumulate_absolute(offset_index: int, aggregate_abs: float) -> float:
        if offset_index == len(data_sequence):
            return aggregate_abs
        current_element = data_sequence[offset_index]
        updated_abs = aggregate_abs + abs(current_element - average_value)
        return accumulate_absolute(offset_index + 1, updated_abs)

    sum_of_elements = sum(data_sequence)
    average_value = sum_of_elements / len(data_sequence)
    total_dev = accumulate_absolute(0, 0.0)
    return total_dev / len(data_sequence)