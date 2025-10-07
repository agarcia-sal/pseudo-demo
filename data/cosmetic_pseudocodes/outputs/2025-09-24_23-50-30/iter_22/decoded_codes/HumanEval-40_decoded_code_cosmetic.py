from typing import Sequence

def triples_sum_to_zero(sequence: Sequence[int]) -> bool:
    n = len(sequence)
    for pointer_a in range(n - 2):
        for pointer_b in range(pointer_a + 1, n - 1):
            pointer_c = pointer_b + 1
            while pointer_c < n:
                if sequence[pointer_a] + sequence[pointer_b] + sequence[pointer_c] == 0:
                    return True
                pointer_c += 1
    return False