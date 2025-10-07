from typing import List


def get_odd_collatz(p: int) -> List[int]:
    q: List[int]
    r: int
    s: int
    t: int
    u: int
    v: int
    w: List[int]

    if p % 2 == 1:
        q = [p]
    else:
        q = []

    r = p

    while r > 1:
        s = r % 2

        if s == 0:
            t = r // 2
        else:
            t = r * 3 + 1

        r = t

        u = r % 2
        if u == 1:
            v = int(r)
            q.append(v)

    w = sorted(q)
    return w