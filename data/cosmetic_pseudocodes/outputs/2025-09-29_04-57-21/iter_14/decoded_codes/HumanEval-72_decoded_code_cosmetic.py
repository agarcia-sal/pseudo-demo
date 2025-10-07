from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    if not (maximum_weight_w >= 0 and maximum_weight_w >= sum(list_q)):
        return False

    left_marker = 0
    right_marker = len(list_q) - 1

    while left_marker < right_marker:
        if list_q[left_marker] != list_q[right_marker]:
            return False
        left_marker += 1
        right_marker -= 1

    return True