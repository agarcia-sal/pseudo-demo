from typing import Sequence

def triples_sum_to_zero(sequence_numbers: Sequence[int]) -> bool:
    n = len(sequence_numbers)
    for pointer_a in range(n - 2):
        for pointer_b in range(pointer_a + 1, n - 1):
            for pointer_c in range(pointer_b + 1, n):
                if sequence_numbers[pointer_c] == -(sequence_numbers[pointer_a] + sequence_numbers[pointer_b]):
                    return True
    return False