from typing import List


def get_odd_collatz(alpha: int) -> List[int]:
    delta: List[int] = []
    if alpha % 2 == 1:
        delta.append(alpha)

    while alpha > 1:
        if alpha % 2 == 0:
            alpha //= 2
        else:
            alpha = 3 * alpha + 1

        if alpha % 2 == 1:
            delta.append(int(alpha))

    return sorted(delta)