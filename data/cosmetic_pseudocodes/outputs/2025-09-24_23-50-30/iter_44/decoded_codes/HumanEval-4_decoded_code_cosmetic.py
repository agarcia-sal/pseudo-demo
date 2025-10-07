from typing import Sequence

def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    def compute_sum(seq: Sequence[float], idx: int, acc: float) -> float:
        if idx == len(seq):
            return acc
        return compute_sum(seq, idx + 1, acc + seq[idx])

    sum_accumulator = compute_sum(sequence_of_values, 0, 0)
    count_elements = len(sequence_of_values)
    average_value = sum_accumulator / count_elements

    def absolute_difference_sum(seq: Sequence[float], idx: int, acc: float) -> float:
        if idx == len(seq):
            return acc
        deviation = seq[idx] - average_value
        positive_deviation = deviation if deviation >= 0 else -deviation
        return absolute_difference_sum(seq, idx + 1, acc + positive_deviation)

    sum_absolute_dev = absolute_difference_sum(sequence_of_values, 0, 0)
    result_value = sum_absolute_dev / count_elements

    return result_value