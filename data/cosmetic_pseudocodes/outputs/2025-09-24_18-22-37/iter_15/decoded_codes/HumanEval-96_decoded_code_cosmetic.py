from typing import List

def count_up_to(q: int) -> List[int]:
    y: List[int] = []
    w: int = 2
    while w < q:
        u: int = 1
        s: int = 2
        while s < w and u == 1:
            v: int = w % s
            if v == 0:
                u = 0
            else:
                _ = 0  # dummy operation to reflect pseudocode structure
            s += 1
        if u == 1:
            y.append(w)
        w += 1
    return y