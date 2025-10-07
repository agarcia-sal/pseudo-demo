from typing import Tuple


def even_odd_palindrome(beta: int) -> Tuple[int, int]:
    def is_palindrome(gamma: int) -> bool:
        s = str(gamma)
        return s == s[::-1]

    alpha = 0
    delta = 0

    def iterate_zeta(zeta: int, eps: int) -> None:
        nonlocal alpha, delta
        if zeta > eps:
            return
        if (zeta % 2 != 0) and is_palindrome(zeta):
            delta += 1
        elif (zeta % 2 == 0) and is_palindrome(zeta):
            alpha += 1
        iterate_zeta(zeta + 1, eps)

    iterate_zeta(1, beta)
    return alpha, delta