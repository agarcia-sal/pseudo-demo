from typing import Sequence


def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    length_value = len(sequence_of_values)
    aggregate = sum(sequence_of_values)
    average = aggregate / length_value

    def compute_sum_of_deviation(current_index: int, accumulator: float) -> float:
        if current_index == length_value:
            return accumulator
        return compute_sum_of_deviation(
            current_index + 1,
            accumulator + abs(sequence_of_values[current_index] - average)
        )

    cumulative_deviation = compute_sum_of_deviation(0, 0.0)
    final_value = cumulative_deviation / length_value
    return final_value