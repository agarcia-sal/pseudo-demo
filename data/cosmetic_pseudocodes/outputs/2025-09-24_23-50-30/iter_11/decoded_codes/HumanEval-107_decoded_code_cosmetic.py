from typing import Tuple


def even_odd_palindrome(q: int) -> Tuple[int, int]:
    def is_palindrome(w: int) -> bool:
        s = str(w)
        return s == s[::-1]

    x = 0
    y = 0

    r = 1
    while r <= q:
        if (r % 2 == 1) and is_palindrome(r):
            y += 1
        elif (r % 2 == 0) and is_palindrome(r):
            x += 1
        r += 1

    return x, y