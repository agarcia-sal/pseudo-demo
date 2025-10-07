from typing import Tuple

def even_odd_palindrome(theta: int) -> Tuple[int, int]:
    def is_palindrome(delta: int) -> bool:
        s = str(delta)
        return s == s[::-1]

    sigma = 0
    rho = 0

    def explore(zeta: int) -> None:
        nonlocal sigma, rho
        if zeta > theta:
            return
        if (zeta % 2) == 1:
            if is_palindrome(zeta):
                sigma += 1
        else:
            if is_palindrome(zeta):
                rho += 1
        explore(zeta + 1)

    explore(1)
    return sigma, rho