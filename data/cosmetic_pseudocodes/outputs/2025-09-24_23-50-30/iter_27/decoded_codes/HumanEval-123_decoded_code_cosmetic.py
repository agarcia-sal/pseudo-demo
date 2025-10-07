from typing import List


def get_odd_collatz(q: int) -> List[int]:
    r: List[int]
    if q % 2 == 0:
        r = []
    else:
        r = [q]

    while q > 1:
        if q % 2 == 0:
            q = q // 2
        else:
            q = 3 * q + 1

        if q % 2 == 1:
            r.append(int(q))

    return sorted(r)