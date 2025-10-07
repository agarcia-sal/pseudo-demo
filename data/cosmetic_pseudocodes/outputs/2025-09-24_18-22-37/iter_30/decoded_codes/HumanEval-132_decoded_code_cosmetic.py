from typing import Sequence

def is_nested(q: Sequence[str]) -> bool:
    p: list[int] = []
    r: list[int] = []
    i: int = 0
    length: int = len(q)

    while i <= length - 1:
        w: str = q[i]
        if w == '[':
            p.append(i)
        else:
            r.append(i)
        i += 1

    r.reverse()

    u: int = 0
    v: int = 0
    x: int = len(r)

    for y in p:
        if v < x and y < r[v]:
            u += 1
            v += 1

    return u >= 2