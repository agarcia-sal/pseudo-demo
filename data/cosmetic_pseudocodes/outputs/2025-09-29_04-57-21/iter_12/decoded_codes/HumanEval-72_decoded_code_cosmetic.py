from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    total_weight = 0
    pos_start = 0
    pos_end = len(list_q) - 1

    while pos_start <= pos_end:
        if pos_start == pos_end:
            total_weight += list_q[pos_start]
        else:
            total_weight += list_q[pos_start] + list_q[pos_end]
        pos_start += 1
        pos_end -= 1

    if total_weight > maximum_weight_w:
        return False

    left_cursor = 0
    right_cursor = len(list_q) - 1

    while left_cursor < right_cursor:
        left_elem = list_q[left_cursor]
        right_elem = list_q[right_cursor]

        if left_elem != right_elem:
            return False

        left_cursor += 1
        right_cursor -= 1

    return True