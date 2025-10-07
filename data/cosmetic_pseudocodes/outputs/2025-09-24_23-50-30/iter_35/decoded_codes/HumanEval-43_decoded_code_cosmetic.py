from typing import Sequence

def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    pos_a: int = 0
    length: int = len(sequence_of_numbers)
    while pos_a < length - 1:
        pos_b: int = pos_a + 1
        while pos_b < length:
            if sequence_of_numbers[pos_a] + sequence_of_numbers[pos_b] == 0:
                return True
            pos_b += 1
        pos_a += 1
    return False