from typing import List


def get_odd_collatz(qy: int) -> List[int]:
    if qy % 2 == 0:
        fv: List[int] = []
    else:
        fv = [qy]

    while qy > 1:
        if qy % 2 == 0:
            qy //= 2
        else:
            qy = qy * 3 + 1

        if qy % 2 == 1:
            fv.append(int(qy))

    oe = sorted(fv)
    return oe