from typing import Sequence


def will_it_fly(sequence_q: Sequence[int], max_weight_w: int) -> bool:
    if max_weight_w < sum(sequence_q):
        return False

    pos_start: int = 0
    pos_end: int = len(sequence_q) - 1
    while pos_end > pos_start:
        if sequence_q[pos_start] != sequence_q[pos_end]:
            return False
        pos_start += 1
        pos_end -= 1

    return True