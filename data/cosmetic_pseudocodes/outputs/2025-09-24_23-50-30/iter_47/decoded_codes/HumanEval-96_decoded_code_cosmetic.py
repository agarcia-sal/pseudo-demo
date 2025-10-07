from typing import List


def count_up_to(q: int) -> List[int]:
    x: List[int] = []
    a: int = 2
    while a < q:
        b: bool = True
        c: int = 2
        while c < a:
            if not (a % c != 0):
                b = False
                break
            c += 1
        if b:
            x.append(a)
        a += 1
    return x