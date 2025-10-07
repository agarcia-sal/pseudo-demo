from typing import Sequence

def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    index_outer: int = 0
    length: int = len(sequence_of_numbers)
    while index_outer < length:
        current_val: int = sequence_of_numbers[index_outer]
        index_inner: int = index_outer + 1
        while index_inner < length:
            candidate_val: int = sequence_of_numbers[index_inner]
            if current_val + candidate_val == 0:
                return True
            index_inner += 1
        index_outer += 1
    return False