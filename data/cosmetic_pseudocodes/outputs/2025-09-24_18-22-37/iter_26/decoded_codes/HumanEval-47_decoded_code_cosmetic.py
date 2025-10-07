from typing import Sequence, Union

def median(original_sequence: Sequence[Union[int, float]]) -> float:
    ordered_sequence = sorted(original_sequence)
    seq_length = len(ordered_sequence)
    half_point = seq_length // 2

    if seq_length % 2 != 0:
        return float(ordered_sequence[half_point])
    else:
        left_mid_index = half_point - 1
        right_mid_index = half_point
        left_value = ordered_sequence[left_mid_index]
        right_value = ordered_sequence[right_mid_index]
        return (left_value + right_value) / 2.0