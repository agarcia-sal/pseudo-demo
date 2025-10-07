from typing import Sequence

def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    def check_pair(pos_a: int) -> bool:
        if pos_a >= len(sequence_of_numbers) - 1:
            return False

        def scan_next(pos_b: int) -> bool:
            if pos_b >= len(sequence_of_numbers):
                return check_pair(pos_a + 1)
            return (sequence_of_numbers[pos_a] + sequence_of_numbers[pos_b] == 0) or scan_next(pos_b + 1)

        return scan_next(pos_a + 1)

    return check_pair(0)