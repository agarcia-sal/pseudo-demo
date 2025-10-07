from typing import Sequence

def mean_absolute_deviation(numbers_sequence: Sequence[float]) -> float:
    count_elements = 0
    accumulated_sum = 0.0
    while True:
        if count_elements >= len(numbers_sequence):
            break
        current_index = count_elements
        accumulated_sum += numbers_sequence[current_index]
        count_elements += 1
    average_var = accumulated_sum / count_elements
    deviation_sum = 0.0
    for idx in range(count_elements):
        temp_diff = numbers_sequence[idx] - average_var
        temp_abs = temp_diff if temp_diff >= 0 else -temp_diff
        deviation_sum += temp_abs
    mad_result = deviation_sum / count_elements
    return mad_result