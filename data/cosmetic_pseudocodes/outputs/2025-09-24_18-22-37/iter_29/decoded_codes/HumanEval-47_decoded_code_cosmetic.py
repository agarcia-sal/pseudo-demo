from typing import Sequence, Union

def median(data_sequence: Sequence[Union[int, float]]) -> float:
    temp_sequence = sorted(data_sequence)
    size_value = len(temp_sequence)
    if size_value % 2 != 0:
        middle_pos = size_value // 2
        return float(temp_sequence[middle_pos])
    else:
        mid_index_a = (size_value // 2) - 1
        mid_index_b = size_value // 2
        sum_middle = temp_sequence[mid_index_a] + temp_sequence[mid_index_b]
        result_median = sum_middle / 2.0
        return result_median