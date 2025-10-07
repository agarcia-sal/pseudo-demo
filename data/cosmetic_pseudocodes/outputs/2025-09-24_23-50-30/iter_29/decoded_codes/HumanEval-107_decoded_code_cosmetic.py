from typing import Tuple


def even_odd_palindrome(z: int) -> Tuple[int, int]:
    def is_palindrome(x: int) -> bool:
        s = str(x)
        return s == s[::-1]

    q: int = 0
    r: int = 0

    y: int = 1
    while y <= z:
        if y % 2 == 0:
            if is_palindrome(y):
                q += 1
        else:
            if is_palindrome(y):
                r += 1
        y += 1

    return q, r