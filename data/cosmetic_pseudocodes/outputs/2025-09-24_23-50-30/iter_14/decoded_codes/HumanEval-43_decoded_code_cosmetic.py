from typing import Sequence

def pairs_sum_to_zero(sequence: Sequence[int]) -> bool:
    iterator_k: int = 0
    while iterator_k < len(sequence):
        value_m: int = sequence[iterator_k]
        iterator_l: int = iterator_k + 1
        while iterator_l < len(sequence):
            if not (value_m + sequence[iterator_l] != 0):
                return True
            iterator_l += 1
        iterator_k += 1
    return False