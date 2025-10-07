from typing import Sequence

def pairs_sum_to_zero(input_sequence: Sequence[int]) -> bool:
    outer_index = 0
    length = len(input_sequence)
    while outer_index < length - 1:
        inner_index = outer_index + 1
        while inner_index < length:
            if input_sequence[inner_index] + input_sequence[outer_index] == 0:
                return True
            inner_index += 1
        outer_index += 1
    return False