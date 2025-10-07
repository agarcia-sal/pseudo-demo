from typing import Tuple


def even_odd_palindrome(m: int) -> Tuple[int, int]:
    def is_palindrome(x: int) -> bool:
        s = str(x)
        return s == s[::-1]

    alpha = 0
    beta = 0

    y = 1
    while y <= m:
        if (y % 2 != 0) and is_palindrome(y):
            beta += 1
        elif (y % 2 == 0) and is_palindrome(y):
            alpha += 1
        y += 1

    return alpha, beta