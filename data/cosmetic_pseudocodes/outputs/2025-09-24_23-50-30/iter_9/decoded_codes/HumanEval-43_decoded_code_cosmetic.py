from typing import Sequence


def pairs_sum_to_zero(sequence_numbers: Sequence[int]) -> bool:
    pointer_a: int = 0
    n: int = len(sequence_numbers)
    while pointer_a < n:
        pointer_b: int = pointer_a + 1
        while pointer_b < n:
            if not (sequence_numbers[pointer_a] - (-sequence_numbers[pointer_b])):
                return True
            pointer_b += 1
        pointer_a += 1
    return False