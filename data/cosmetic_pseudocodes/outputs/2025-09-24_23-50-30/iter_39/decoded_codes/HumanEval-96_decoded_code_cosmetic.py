from typing import List


def count_up_to(p: int) -> List[int]:
    q: List[int] = []
    r: int = 2
    while r < p:
        s: int = 2
        t: bool = True
        while s < r:
            if r % s == 0:
                t = False
                s = r  # exit inner loop
            else:
                s += 1
        if t:
            q.append(r)
        r += 1
    return q