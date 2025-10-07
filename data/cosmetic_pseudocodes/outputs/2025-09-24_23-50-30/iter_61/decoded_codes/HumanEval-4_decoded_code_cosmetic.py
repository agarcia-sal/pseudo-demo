from typing import Sequence


def mean_absolute_deviation(array_input: Sequence[float]) -> float:
    if not array_input:
        return 0.0

    def accumulate_absolute_values(i: int, current_sum: float) -> float:
        if i >= len(array_input):
            return current_sum
        return accumulate_absolute_values(i + 1, current_sum + abs(array_input[i] - avg))

    sum_total = 0.0
    index_counter = 0
    while index_counter < len(array_input):
        sum_total += array_input[index_counter]
        index_counter += 1

    avg = sum_total / len(array_input)
    total_deviation = accumulate_absolute_values(0, 0.0)

    mad_result = total_deviation / len(array_input)
    return mad_result