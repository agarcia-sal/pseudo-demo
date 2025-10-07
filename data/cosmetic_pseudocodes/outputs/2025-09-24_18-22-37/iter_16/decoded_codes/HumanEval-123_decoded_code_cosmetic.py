from typing import List


def get_odd_collatz(q: int) -> List[int]:
    p: List[int]
    if q % 2 != 1:
        p = []
    else:
        p = [q]

    while q > 1:
        if q % 2 == 0:
            r = q // 2
            q = r
        else:
            s = (q * 3) + 1
            q = s

        if q % 2 == 1:
            p.append(int(q))

    return sorted(p)