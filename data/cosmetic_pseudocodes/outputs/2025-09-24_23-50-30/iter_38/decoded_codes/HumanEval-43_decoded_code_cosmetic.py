from typing import Sequence

def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    def search_offset(position_a: int) -> bool:
        if position_a == len(sequence_of_numbers):
            return False

        def search_partner(position_b: int) -> bool:
            if position_b == len(sequence_of_numbers):
                return search_offset(position_a + 1)
            return (sequence_of_numbers[position_a] + sequence_of_numbers[position_b] == 0) or search_partner(position_b + 1)

        return search_partner(position_a + 1)

    return search_offset(0)