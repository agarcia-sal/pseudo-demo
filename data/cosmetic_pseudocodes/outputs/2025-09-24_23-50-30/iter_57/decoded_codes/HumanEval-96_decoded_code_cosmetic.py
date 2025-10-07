from typing import List


def count_up_to(q: int) -> List[int]:
    A: List[int] = []
    w: int = 2
    while w < q:
        B: bool = True
        c: int = 2
        while c < w:
            if w % c == 0:
                B = False
                break
            else:
                c += 1
        if B:
            A.append(w)
        w += 1
    return A