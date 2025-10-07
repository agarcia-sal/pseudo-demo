from typing import Sequence

def mean_absolute_deviation(sequence_x: Sequence[float]) -> float:
    n = len(sequence_x)
    if n == 0:
        raise ValueError("mean_absolute_deviation() arg is an empty sequence")
    aggregate_y = sum(sequence_x)
    pivot_w = aggregate_y / n
    aggregate_q = sum(abs(item_r - pivot_w) for item_r in sequence_x)
    result_s = aggregate_q / n
    return result_s