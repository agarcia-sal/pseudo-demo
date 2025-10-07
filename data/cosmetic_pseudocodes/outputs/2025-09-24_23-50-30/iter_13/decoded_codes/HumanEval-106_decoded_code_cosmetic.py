from typing import List

def f(m: int) -> List[int]:
    o: List[int] = []
    p: int = 1
    for q in range(1, m + 1):
        if q % 2 != 0:
            r: int = (q * (q + 1)) // 2
            o.append(r)
            continue
        p = 1
        for s in range(1, q + 1):
            p *= s
        o.append(p)
    return o