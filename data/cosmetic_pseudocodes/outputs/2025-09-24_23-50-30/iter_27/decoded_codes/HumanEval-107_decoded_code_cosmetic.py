from typing import Tuple


def even_odd_palindrome(alpha: int) -> Tuple[int, int]:
    def is_palindrome(beta: int) -> bool:
        s = str(beta)
        return s == s[::-1]

    kappa = 0  # count of even palindromic numbers
    omega = 0  # count of odd palindromic numbers

    rho = 1
    while rho <= alpha:
        if (rho % 2 == 1) and is_palindrome(rho):
            omega += 1
        elif (rho % 2 == 0) and is_palindrome(rho):
            kappa += 1
        rho += 1

    return kappa, omega