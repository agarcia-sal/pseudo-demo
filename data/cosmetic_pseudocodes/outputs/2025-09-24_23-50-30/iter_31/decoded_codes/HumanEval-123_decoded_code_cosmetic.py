from typing import List


def get_odd_collatz(z: int) -> List[int]:
    v: List[int] = [] if z % 2 == 0 else [z]

    while z > 1:
        if z % 2 == 0:
            z = z // 2
        else:
            z = z * 3 + 1

        if z % 2 == 1:
            v.append(int(z))

    return sorted(v)