from typing import List

def will_it_fly(q: List[int], w: int) -> bool:
    if sum(q) > w:
        return False
    i = 0
    j = len(q) - 1
    while i < j:
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1
    return True