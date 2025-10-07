from typing import List

def count_up_to(q: int) -> List[int]:
    y: List[int] = []
    u: int = 2
    while u < q:
        r: bool = True
        v: int = 2
        while v < u:
            if u % v == 0:
                r = False
                break
            v += 1
        if r:
            y.append(u)
        u += 1
    return y