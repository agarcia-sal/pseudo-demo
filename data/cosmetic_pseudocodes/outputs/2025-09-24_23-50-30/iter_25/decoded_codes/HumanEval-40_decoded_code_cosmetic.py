from typing import Sequence

def triples_sum_to_zero(sequence: Sequence[int]) -> bool:
    length = len(sequence)
    outer_index = 0
    while outer_index < length - 2:
        middle_index = outer_index + 1
        while middle_index < length - 1:
            inner_index = middle_index + 1
            while inner_index < length:
                # Check if sum of the triplet equals zero
                if sequence[outer_index] + sequence[middle_index] + sequence[inner_index] == 0:
                    return True
                inner_index += 1
            middle_index += 1
        outer_index += 1
    return False