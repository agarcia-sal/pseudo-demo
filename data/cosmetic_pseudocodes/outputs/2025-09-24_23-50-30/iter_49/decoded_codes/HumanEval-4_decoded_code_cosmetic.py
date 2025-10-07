from typing import Sequence


def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    def compute_average(pointer: int, acc_total: float) -> float:
        if pointer == len(sequence_of_values):
            return acc_total / len(sequence_of_values)
        return compute_average(pointer + 1, acc_total + sequence_of_values[pointer])

    average_metric: float = compute_average(0, 0)

    def accumulate_differences(index_tracker: int, acc_sum: float) -> float:
        if index_tracker == len(sequence_of_values):
            return acc_sum
        current_difference = abs(sequence_of_values[index_tracker] - average_metric)
        return accumulate_differences(index_tracker + 1, acc_sum + current_difference)

    accumulated_diff_sum: float = accumulate_differences(0, 0)
    final_result: float = accumulated_diff_sum / len(sequence_of_values)
    return final_result