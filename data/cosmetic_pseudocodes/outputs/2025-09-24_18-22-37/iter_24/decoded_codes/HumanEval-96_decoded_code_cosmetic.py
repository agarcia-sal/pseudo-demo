from typing import List


def count_up_to(c: int) -> List[int]:
    o: List[int] = []
    z: int = 2
    while z < c:
        q: bool = True
        s: int = 2
        while s < z:
            if z % s == 0:
                q = False
                s = z  # exit inner loop early
            else:
                s += 1
        if q:
            o.append(z)
        z += 1
    return o