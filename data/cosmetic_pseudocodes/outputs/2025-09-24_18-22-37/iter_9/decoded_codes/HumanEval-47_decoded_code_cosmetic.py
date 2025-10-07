from typing import Sequence, Union

def median(data_sequence: Sequence[Union[int, float]]) -> float:
    sorted_sequence = sorted(data_sequence)
    seq_length = len(sorted_sequence)
    mid_index = seq_length // 2

    if seq_length % 2 != 0:
        return float(sorted_sequence[mid_index])
    else:
        left_value = sorted_sequence[mid_index - 1]
        right_value = sorted_sequence[mid_index]
        return (left_value + right_value) / 2.0