from typing import Sequence

def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    def finder(position_a: int, position_b: int) -> bool:
        if position_a >= len(sequence_of_numbers):
            return False
        if position_b >= len(sequence_of_numbers):
            return finder(position_a + 1, position_a + 2)
        if sequence_of_numbers[position_a] + sequence_of_numbers[position_b] == 0:
            return True
        return finder(position_a, position_b + 1)

    return finder(0, 1)