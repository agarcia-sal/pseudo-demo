from typing import Sequence, Union

def median(input_sequence: Sequence[Union[int, float]]) -> float:
    temp_array = list(input_sequence)
    sorted_array = sorted(temp_array)
    count = len(sorted_array)
    half_index = count // 2

    if count % 2 != 0:
        return float(sorted_array[half_index])
    else:
        left_val = sorted_array[half_index - 1]
        right_val = sorted_array[half_index]
        return (left_val + right_val) / 2.0