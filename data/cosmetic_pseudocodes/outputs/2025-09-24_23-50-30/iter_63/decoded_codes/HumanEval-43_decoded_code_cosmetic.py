from typing import Sequence

def pairs_sum_to_zero(values_sequence: Sequence[int]) -> bool:
    length = len(values_sequence)
    for index_outer in range(length - 1):
        for index_inner in range(index_outer + 1, length):
            combined = values_sequence[index_inner] + values_sequence[index_outer]
            if combined == 0:
                return True
    return False