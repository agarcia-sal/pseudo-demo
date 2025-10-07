from typing import List

def f(p: int) -> List[int]:
    q: List[int] = []
    s: int = 1

    while s <= p:
        if s % 2 == 0:
            t: int = 1
            u: int = 1
            while u <= s:
                t *= u
                u += 1
            q.append(t)
        else:
            v: int = 0
            w: int = 1
            while w <= s:
                v += w
                w += 1
            q.append(v)
        s += 1

    return q