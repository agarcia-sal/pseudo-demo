from typing import Sequence

def pairs_sum_to_zero(input_sequence: Sequence[int]) -> bool:
    outer_idx: int = 0
    length: int = len(input_sequence)
    while outer_idx < length - 1:
        inner_idx: int = outer_idx + 1
        while inner_idx < length:
            if input_sequence[outer_idx] + input_sequence[inner_idx] == 0:
                return True
            inner_idx += 1
        outer_idx += 1
    return False