from typing import Sequence


def pairs_sum_to_zero(sequence: Sequence[int]) -> bool:
    position_a: int = 0
    while position_a < len(sequence) - 1:
        position_b: int = position_a + 1
        while position_b < len(sequence):
            if sequence[position_b] + sequence[position_a] == 0:
                return True
            position_b += 1
        position_a += 1
    return False