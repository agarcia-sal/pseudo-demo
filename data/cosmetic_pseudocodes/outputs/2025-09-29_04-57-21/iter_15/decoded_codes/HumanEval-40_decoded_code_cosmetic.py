from typing import Sequence

def triples_sum_to_zero(number_sequence: Sequence[int]) -> bool:
    length = len(number_sequence)
    for position_a in range(length):
        for position_b in range(position_a + 1, length):
            for position_c in range(position_b + 1, length):
                total_sum = (
                    number_sequence[position_a]
                    + number_sequence[position_b]
                    + number_sequence[position_c]
                )
                if total_sum == 0:
                    return True
    return False