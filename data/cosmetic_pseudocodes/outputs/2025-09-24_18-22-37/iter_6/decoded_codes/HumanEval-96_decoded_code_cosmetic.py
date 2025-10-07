from typing import List

def count_up_to(q: int) -> List[int]:
    r: List[int] = []
    s: int = 2
    while s < q:
        t: bool = True
        u: int = 2
        while u < s:
            if s % u == 0:
                t = False
                break
            else:
                u += 1
        if t:
            r.append(s)
        s += 1
    return r