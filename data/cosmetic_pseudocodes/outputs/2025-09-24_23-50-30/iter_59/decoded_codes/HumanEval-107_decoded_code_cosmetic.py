from typing import Tuple


def even_odd_palindrome(p: int) -> Tuple[int, int]:
    def is_palindrome(q: int) -> bool:
        s = str(q)
        return s == s[::-1]

    a = 0  # count of even palindrome numbers
    b = 0  # count of odd palindrome numbers

    c = 1
    while c <= p:
        if (c % 2 == 1) and is_palindrome(c):
            b += 1
        elif (c % 2 == 0) and is_palindrome(c):
            a += 1
        c += 1

    return a, b