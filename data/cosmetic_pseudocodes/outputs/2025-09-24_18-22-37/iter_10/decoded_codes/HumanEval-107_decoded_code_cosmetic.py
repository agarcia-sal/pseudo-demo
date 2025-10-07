from typing import Tuple


def even_odd_palindrome(m: int) -> Tuple[int, int]:
    def is_palindrome(q: int) -> bool:
        s = str(q)
        r = s[::-1]
        return s == r

    h = 0  # count of even palindromes
    g = 0  # count of odd palindromes

    j = 1
    while j <= m:
        u = j % 2
        if u == 0:
            if is_palindrome(j):
                h += 1
        else:
            if is_palindrome(j):
                g += 1
        j += 1

    return h, g