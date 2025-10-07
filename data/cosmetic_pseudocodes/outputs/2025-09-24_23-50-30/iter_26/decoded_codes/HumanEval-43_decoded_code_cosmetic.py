from typing import Sequence


def pairs_sum_to_zero(sequence_numbers: Sequence[int]) -> bool:
    def search_pair(position_start: int) -> bool:
        if position_start >= len(sequence_numbers):
            return False

        def check_next(position_compare: int) -> bool:
            if position_compare >= len(sequence_numbers):
                return False
            elif sequence_numbers[position_start] + sequence_numbers[position_compare] == 0:
                return True
            else:
                return check_next(position_compare + 1)

        if check_next(position_start + 1):
            return True
        else:
            return search_pair(position_start + 1)

    return search_pair(0)