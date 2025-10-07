from typing import List

def will_it_fly(list_q: List[int], max_weight: int) -> bool:
    if sum(list_q) > max_weight:
        return False

    i: int = 0
    j: int = len(list_q) - 1

    while i < j:
        if list_q[i] != list_q[j]:
            return False
        i += 1
        j -= 1

    return True