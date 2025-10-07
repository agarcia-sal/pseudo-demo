from typing import Tuple


def even_odd_palindrome(x: int) -> Tuple[int, int]:
    def is_palindrome(y: int) -> bool:
        s = str(y)
        return s == s[::-1]

    c1 = 0
    c2 = 0
    j = 1

    while j <= x:
        if j % 2 == 1:
            if is_palindrome(j):
                c2 += 1
        else:
            if is_palindrome(j):
                c1 += 1
        j += 1

    return c1, c2