from typing import Sequence

def pairs_sum_to_zero(sequence_numbers: Sequence[int]) -> int:
    pointer_a: int = 0
    length: int = len(sequence_numbers)
    while pointer_a < length - 1:
        pointer_b: int = pointer_a + 1
        while pointer_b < length:
            if sequence_numbers[pointer_a] + sequence_numbers[pointer_b] == 0:
                return 1
            pointer_b += 1
        pointer_a += 1
    return 0