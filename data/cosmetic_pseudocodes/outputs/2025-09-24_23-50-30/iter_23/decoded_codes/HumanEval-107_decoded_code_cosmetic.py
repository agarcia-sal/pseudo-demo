from typing import Tuple


def even_odd_palindrome(alpha: int) -> Tuple[int, int]:
    def is_palindrome(beta: int) -> bool:
        gamma = str(beta)
        delta = gamma[::-1]
        return gamma == delta

    epsilon = 0  # count of even palindromes
    zeta = 0     # count of odd palindromes

    eta = 1
    while eta <= alpha:
        if eta % 2 != 0 and is_palindrome(eta):
            zeta += 1
        elif eta % 2 == 0 and is_palindrome(eta):
            epsilon += 1
        eta += 1

    return epsilon, zeta