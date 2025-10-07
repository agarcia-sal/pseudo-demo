from typing import Sequence

def mean_absolute_deviation(input_sequence: Sequence[float]) -> float:
    count_vars: int = 0
    aggregate_total: float = 0.0
    length: int = len(input_sequence)
    if length == 0:
        raise ValueError("input_sequence must not be empty")
    while count_vars < length:
        aggregate_total += input_sequence[count_vars]
        count_vars += 1

    average_val: float = aggregate_total * (1 / length)

    index_ptr: int = 0
    deviation_sum: float = 0.0
    while index_ptr < length:
        gap: float = input_sequence[index_ptr] - average_val
        absolute_gap: float = -gap if gap < 0 else gap
        deviation_sum += absolute_gap
        index_ptr += 1

    result_val: float = deviation_sum * (1 / length)
    return result_val