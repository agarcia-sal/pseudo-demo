from typing import List

def f(w: int) -> List[int]:
    x: List[int] = []
    y: int = 1
    z: int = 0
    q: int = 1
    while q <= w:
        if q % 2 != 1:
            y = 1
            p = 1
            while p <= q:
                y *= p
                p += 1
            x.append(y)
        else:
            z = 0
            r = 1
            while r <= q:
                z += r
                r += 1
            x.append(z)
        q += 1
    return x