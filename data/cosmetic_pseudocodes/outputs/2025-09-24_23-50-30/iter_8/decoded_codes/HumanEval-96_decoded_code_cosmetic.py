from typing import List

def count_up_to(z: int) -> List[int]:
    q: List[int] = []
    x: int = 2
    while x < z:
        c: int = 0
        v: int = 2
        while v < x:
            if x - v * (x // v) == 0:
                c += 1
                v = x  # break inner loop early
            else:
                v += 1
        if c == 0:
            q.append(x)
        x += 1
    return q