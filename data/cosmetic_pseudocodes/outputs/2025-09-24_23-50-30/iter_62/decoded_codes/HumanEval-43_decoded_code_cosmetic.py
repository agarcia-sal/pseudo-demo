from typing import Sequence


def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    def check_pair(position_x: int) -> bool:
        if position_x >= len(sequence_of_numbers):
            return False

        def scan_next(position_y: int) -> bool:
            if position_y >= len(sequence_of_numbers):
                return check_pair(position_x + 1)
            if sequence_of_numbers[position_x] + sequence_of_numbers[position_y] == 0:
                return True
            return scan_next(position_y + 1)

        return scan_next(position_x + 1)

    return check_pair(0)