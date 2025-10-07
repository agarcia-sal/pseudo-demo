from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(x: int) -> bool:
        str_x: str = str(x)
        rev_str_x: str = ""
        p: int = len(str_x) - 1
        while p >= 0:
            rev_str_x += str_x[p]
            p -= 1
        return str_x == rev_str_x

    a: int = 0
    b: int = 0
    c: int = 1

    while c <= n:
        d: int = c % 2
        e: bool = is_palindrome(c)

        if e:
            if d != 0:
                b += 1
            else:
                a += 1

        c += 1

    return a, b