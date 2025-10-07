from typing import Sequence


def pairs_sum_to_zero(sequence_of_values: Sequence[int]) -> bool:
    def check_pair(pos_a: int, pos_b: int) -> bool:
        if pos_a >= len(sequence_of_values) - 1:
            return False
        if pos_b >= len(sequence_of_values):
            return check_pair(pos_a + 1, pos_a + 2)
        if sequence_of_values[pos_a] + sequence_of_values[pos_b] == 0:
            return True
        return check_pair(pos_a, pos_b + 1)

    return check_pair(0, 1)