from typing import Tuple


def even_odd_palindrome(q: int) -> Tuple[int, int]:
    def is_palindrome(w: int) -> bool:
        s = str(w)
        return s == s[::-1]

    a: int = 0  # count of even palindromes
    b: int = 0  # count of odd palindromes
    c: int = 1

    while c < q + 1:
        if c % 2 == 1:
            if is_palindrome(c):
                b += 1
        else:
            if is_palindrome(c):
                a += 1
        c += 1

    return a, b