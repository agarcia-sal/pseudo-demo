from typing import List

def count_up_to(q: int) -> List[int]:
    y = 0
    z: List[int] = []
    while y < q - 2:
        w = True
        s = 1
        y += 2
        while s < y - 1 and w:
            if y % (s + 1) == 0:
                w = False
            else:
                s += 1
        v = w
        if v:
            z.append(y)
    return z