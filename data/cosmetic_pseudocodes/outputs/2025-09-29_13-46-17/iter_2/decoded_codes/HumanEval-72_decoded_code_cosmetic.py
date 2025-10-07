from typing import List

def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    def helper(left_idx: int, right_idx: int) -> bool:
        if left_idx >= right_idx:
            return True
        if list_q[left_idx] != list_q[right_idx]:
            return False
        return helper(left_idx + 1, right_idx - 1)

    if maximum_weight_w < sum(list_q):
        return False

    return helper(0, len(list_q) - 1)