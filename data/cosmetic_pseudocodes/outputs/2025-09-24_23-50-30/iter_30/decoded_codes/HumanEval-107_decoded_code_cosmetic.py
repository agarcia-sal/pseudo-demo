from typing import Tuple


def even_odd_palindrome(m: int) -> Tuple[int, int]:
    def is_palindrome(p: int) -> bool:
        s = str(p)
        return s == s[::-1]

    x1: int = 0  # count of even palindromes
    x2: int = 0  # count of odd palindromes

    for q in range(1, m + 1):
        if q % 2 == 1:
            if is_palindrome(q):
                x2 += 1
        else:
            if is_palindrome(q):
                x1 += 1

    return x1, x2