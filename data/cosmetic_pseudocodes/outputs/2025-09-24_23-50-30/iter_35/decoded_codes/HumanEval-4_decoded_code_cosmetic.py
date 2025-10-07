from typing import Sequence

def mean_absolute_deviation(array_numbers: Sequence[float]) -> float:
    len_count: int = len(array_numbers)
    if len_count == 0:
        raise ValueError("mean_absolute_deviation() arg is an empty sequence")
    total_sum: float = 0.0
    idx_counter: int = 0
    while idx_counter < len_count:
        total_sum += array_numbers[idx_counter]
        idx_counter += 1
    average_val: float = total_sum / len_count
    acc_abs_diff: float = 0.0
    idx_counter = 0
    while True:
        temp_diff: float = array_numbers[idx_counter] - average_val
        abs_diff: float = temp_diff if temp_diff >= 0 else -temp_diff
        acc_abs_diff += abs_diff
        idx_counter += 1
        if idx_counter >= len_count:
            break
    final_value: float = acc_abs_diff / len_count
    return final_value