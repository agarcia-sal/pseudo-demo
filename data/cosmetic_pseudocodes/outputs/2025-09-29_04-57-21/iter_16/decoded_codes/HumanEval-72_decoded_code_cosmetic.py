from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    if maximum_weight_w < sum(list_q):
        return False

    head_pos: int = 0
    tail_pos: int = len(list_q) - 1

    while head_pos < tail_pos:
        if list_q[head_pos] != list_q[tail_pos]:
            return False
        head_pos += 1
        tail_pos -= 1

    return True