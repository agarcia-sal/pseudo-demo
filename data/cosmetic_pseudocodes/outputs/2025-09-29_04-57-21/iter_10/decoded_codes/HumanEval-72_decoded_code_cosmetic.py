from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    if maximum_weight_w < 0 or maximum_weight_w < sum(list_q):
        return False

    left_ptr = 0
    right_ptr = len(list_q) - 1

    while left_ptr < right_ptr:
        if list_q[left_ptr] != list_q[right_ptr]:
            return False
        left_ptr += 1
        right_ptr -= 1

    return True