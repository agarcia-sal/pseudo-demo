from typing import Tuple


def even_odd_palindrome(p: int) -> Tuple[int, int]:
    def is_palindrome(q: int) -> bool:
        u = str(q)
        v = u[::-1]
        return u == v

    alpha: int = 0
    beta: int = 0

    zeta: int = 1
    while zeta <= p:
        gamma: int = zeta % 2
        delta: bool = is_palindrome(zeta)

        if delta:
            if gamma == 1:
                beta += 1
            elif gamma == 0:
                alpha += 1
        zeta += 1

    return alpha, beta