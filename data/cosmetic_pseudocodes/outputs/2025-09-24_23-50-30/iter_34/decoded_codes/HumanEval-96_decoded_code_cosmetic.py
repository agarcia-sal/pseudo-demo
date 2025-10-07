from typing import List

def count_up_to(w: int) -> List[int]:
    q: List[int] = []
    r: int = 2
    while r < w:
        s: int = 1
        t: int = 2
        while t < r and s == 1:
            if r % t == 0:
                s = 0
            if s == 0:
                t = w  # exit inner loop immediately
            else:
                t += 1
        if s == 1:
            q.append(r)
        r += 1
    return q