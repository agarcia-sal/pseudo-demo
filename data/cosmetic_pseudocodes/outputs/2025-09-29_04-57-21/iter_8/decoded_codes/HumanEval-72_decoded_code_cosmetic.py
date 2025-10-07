from typing import Sequence

def will_it_fly(sequence_s: Sequence[int], limit_L: int) -> bool:
    if limit_L < sum(sequence_s):
        return False

    start_pos: int = 0
    end_pos: int = len(sequence_s) - 1
    while start_pos < end_pos:
        if sequence_s[start_pos] != sequence_s[end_pos]:
            return False
        start_pos += 1
        end_pos -= 1
    return True