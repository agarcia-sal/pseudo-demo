from typing import List


def count_up_to(x: int) -> List[int]:
    w: int = 2
    s: List[int] = []
    while w < x:
        q: int = 2
        r: bool = True
        while q < w and r:
            if w % q == 0:
                r = False
            else:
                r = r and True  # redundant but kept to reflect pseudocode
            if not r:
                q = x  # break inner loop by forcing q >= w
            else:
                q += 1
        if r:
            s.append(w)
        w += 1
    return s