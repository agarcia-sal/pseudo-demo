from typing import Sequence


def pairs_sum_to_zero(sequence_numbers: Sequence[int]) -> bool:
    def check_next(offset: int) -> bool:
        if offset >= len(sequence_numbers):
            return False
        for current_pos in range(offset):
            if sequence_numbers[offset] + sequence_numbers[current_pos] == 0:
                return True
        return check_next(offset + 1)

    return check_next(1)