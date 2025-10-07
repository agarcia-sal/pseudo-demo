from typing import Tuple

def even_odd_palindrome(p: int) -> Tuple[int, int]:
    def is_palindrome(q: int) -> bool:
        s = str(q)
        return s == s[::-1]

    a = 0
    b = 0

    def loop(r: int) -> Tuple[int, int]:
        nonlocal a, b
        if r > p:
            return a, b
        odd = (r % 2 == 1)
        palindrome = is_palindrome(r)
        if palindrome:
            if odd:
                b += 1
            else:
                a += 1
        return loop(r + 1)

    return loop(1)