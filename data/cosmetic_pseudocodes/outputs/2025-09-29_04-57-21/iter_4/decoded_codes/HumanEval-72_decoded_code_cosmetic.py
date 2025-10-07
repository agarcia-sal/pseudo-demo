from typing import Sequence

def will_it_fly(sequence_q: Sequence[int], max_capacity_w: int) -> bool:
    if max_capacity_w < sum(sequence_q):
        return False

    start_pos: int = 0
    end_pos: int = len(sequence_q) - 1

    while start_pos < end_pos:
        if sequence_q[start_pos] != sequence_q[end_pos]:
            return False
        start_pos += 1
        end_pos -= 1

    return True