from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    total_weight: int = sum(list_q)
    if total_weight > maximum_weight_w:
        return False

    left_ptr: int = 0
    right_ptr: int = len(list_q) - 1

    while left_ptr < right_ptr:
        if list_q[left_ptr] != list_q[right_ptr]:
            return False
        left_ptr += 1
        right_ptr -= 1

    return True