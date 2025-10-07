from typing import List

def f(x: int) -> List[int]:
    q: List[int] = []
    p = 1
    for r in range(1, x + 1):
        if r % 2 != 1:
            p = 1
            s = 1
            while s <= r:
                p *= s
                s += 1
            q.append(p)
        else:
            t = 0
            u = 1
            while u <= r:
                t += u
                u += 1
            q.append(t)
    return q