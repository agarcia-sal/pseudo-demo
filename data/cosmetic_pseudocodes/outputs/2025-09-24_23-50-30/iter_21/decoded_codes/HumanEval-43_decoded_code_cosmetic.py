from typing import Sequence

def pairs_sum_to_zero(input_sequence: Sequence[int]) -> bool:
    def has_zero_sum_pair(current_pos: int) -> bool:
        if current_pos >= len(input_sequence) - 1:
            return False

        def check_pairs(offset: int) -> bool:
            if offset >= len(input_sequence):
                return False
            if input_sequence[current_pos] + input_sequence[offset] == 0:
                return True
            return check_pairs(offset + 1)

        if check_pairs(current_pos + 1):
            return True
        return has_zero_sum_pair(current_pos + 1)

    return has_zero_sum_pair(0)