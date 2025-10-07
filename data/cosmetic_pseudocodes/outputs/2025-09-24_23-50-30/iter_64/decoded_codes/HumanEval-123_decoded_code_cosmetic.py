from typing import List


def get_odd_collatz(alpha: int) -> List[int]:
    omega: List[int] = [] if alpha % 2 == 0 else [alpha]

    while True:
        if alpha <= 1:
            break

        if alpha % 2 == 0:
            alpha //= 2
        else:
            alpha = 3 * alpha + 1

        if alpha % 2 == 1:
            omega.append(alpha)

    return sorted(omega)