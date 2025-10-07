from typing import Tuple

def even_odd_palindrome(alpha: int) -> Tuple[int, int]:
    def is_palindrome(beta: int) -> bool:
        s = str(beta)
        return s == s[::-1]

    def count_palindromes(delta: int, gamma: int, epsilon: int, zeta: int) -> Tuple[int, int]:
        if delta > alpha:
            return gamma, epsilon
        if (delta % 2) == 1 and is_palindrome(delta):
            iota = epsilon + 1
            return count_palindromes(delta + 1, gamma, iota, zeta)
        if (delta % 2) == 0 and is_palindrome(delta):
            kappa = gamma + 1
            return count_palindromes(delta + 1, kappa, epsilon, zeta)
        return count_palindromes(delta + 1, gamma, epsilon, zeta)

    return count_palindromes(1, 0, 0, 0)