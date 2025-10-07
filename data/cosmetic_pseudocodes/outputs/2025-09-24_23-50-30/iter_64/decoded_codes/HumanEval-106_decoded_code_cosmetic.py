from typing import List

def f(p: int) -> List[int]:
    r: List[int] = []
    q: int = 1
    while q <= p:
        if q % 2 == 0:
            x: int = 1
            k: int = 1
            while k <= q:
                x *= k
                k += 1
            r.append(x)
        else:
            y: int = 0
            a: int = 1
            while a <= q:
                y += a
                a += 1
            r.append(y)
        q += 1
    return r