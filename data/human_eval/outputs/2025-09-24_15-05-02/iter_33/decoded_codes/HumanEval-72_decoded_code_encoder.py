from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    if sum(list_q) > maximum_weight_w:
        return False
    i, j = 0, len(list_q) - 1
    while i < j:
        if list_q[i] != list_q[j]:
            return False
        i += 1
        j -= 1
    return True