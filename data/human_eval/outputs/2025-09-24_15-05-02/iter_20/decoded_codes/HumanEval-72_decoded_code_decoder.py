from typing import Sequence

def will_it_fly(q: Sequence[int], w: int) -> bool:
    if sum(q) > w:
        return False

    i, j = 0, len(q) - 1
    while i < j:
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1

    return True