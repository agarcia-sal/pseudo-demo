from typing import Sequence


def triples_sum_to_zero(sequence: Sequence[int]) -> bool:
    length = len(sequence)
    for position_a in range(length - 2):
        for position_b in range(position_a + 1, length - 1):
            target = -(sequence[position_a] + sequence[position_b])
            for position_c in range(position_b + 1, length):
                if sequence[position_c] == target:
                    return True
    return False