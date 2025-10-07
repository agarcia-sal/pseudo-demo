from typing import Tuple


def even_odd_palindrome(m: int) -> Tuple[int, int]:
    def is_palindrome(k: int) -> bool:
        a = str(k)
        b = a[::-1]
        return a == b

    p = 0
    q = 0

    def recur(r: int, s: int, t: int) -> Tuple[int, int]:
        if r > m:
            return s, t
        cond1 = (r % 2 != 0) and is_palindrome(r)
        cond2 = (r % 2 == 0) and is_palindrome(r)
        return recur(
            r + 1,
            s + (1 if cond2 else 0),
            t + (1 if cond1 else 0),
        )

    return recur(1, p, q)