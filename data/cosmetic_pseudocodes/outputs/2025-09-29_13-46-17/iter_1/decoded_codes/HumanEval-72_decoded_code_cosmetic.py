from typing import List

def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    if maximum_weight_w < sum(list_q):
        return False

    left_pointer: int = 0
    right_pointer: int = len(list_q) - 1

    while left_pointer < right_pointer:
        if list_q[left_pointer] != list_q[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1

    return True