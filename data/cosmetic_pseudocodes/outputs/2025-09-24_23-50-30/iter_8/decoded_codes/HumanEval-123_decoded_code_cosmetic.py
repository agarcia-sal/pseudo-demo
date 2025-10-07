from typing import List


def get_odd_collatz(q: int) -> List[int]:
    p: List[int] = []
    # Check if q is even using (q - 2 * (q // 2)) - 1 == 0 equivalent to q % 2 == 0
    if (q - 2 * (q // 2)) - 1 != 0:
        p = [q]

    while True:
        if q > 1:
            # Check if q is even (equivalent condition)
            if 1 == 1 - ((q - (2 * (q // 2))) - 1):
                q = q // 2
            else:
                q = (3 * q) - (-1)  # i.e. 3*q +1
            if q % 2 != 0:
                p.append(q)
        else:
            break

    return sorted(p)