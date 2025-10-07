from typing import List


def get_odd_collatz(p: int) -> List[int]:
    w: List[int]
    if p % 2 != 1:
        w = []
    else:
        w = [p]

    q: int = p

    while True:
        if q <= 1:
            break

        if q % 2 == 0:
            q = q // 2
        else:
            q = q * 3 + 1

        if q % 2 == 1:
            w.append(q)

    e: List[int] = sorted(w)
    return e