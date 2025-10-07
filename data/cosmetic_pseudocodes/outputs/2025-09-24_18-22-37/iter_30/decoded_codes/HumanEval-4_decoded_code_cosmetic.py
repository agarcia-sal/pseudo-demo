from typing import Sequence

def mean_absolute_deviation(seq_values: Sequence[float]) -> float:
    count_vals: int = len(seq_values)
    if count_vals == 0:
        raise ValueError("seq_values must not be empty")
    aggregate_sum: float = 0.0
    idx: int = 0
    while idx < count_vals:
        current_val: float = seq_values[idx]
        aggregate_sum += current_val
        idx += 1
    average_val: float = aggregate_sum / count_vals

    sum_diff_abs: float = 0.0
    pos: int = 0
    while pos < count_vals:
        val_element: float = seq_values[pos]
        difference: float = val_element - average_val
        absolute_diff: float = difference
        if absolute_diff < 0:
            absolute_diff = -absolute_diff
        sum_diff_abs += absolute_diff
        pos += 1

    mad_result: float = sum_diff_abs / count_vals
    return mad_result