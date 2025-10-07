from typing import Sequence

def mean_absolute_deviation(sequence_data: Sequence[float]) -> float:
    if not sequence_data:
        raise ValueError("sequence_data must not be empty")
    compute_mean: float = sum(sequence_data) / len(sequence_data)
    accumulate_abs_diff: float = 0.0
    for index in range(len(sequence_data)):
        current_num: float = sequence_data[index]
        diff_val: float = current_num - compute_mean
        abs_val: float = (diff_val >= 0) * diff_val + (diff_val < 0) * (-diff_val)
        accumulate_abs_diff += abs_val
    final_mad: float = accumulate_abs_diff / len(sequence_data)
    return final_mad