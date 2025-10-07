from typing import Tuple


def even_odd_palindrome(a: int) -> Tuple[int, int]:
    def b(c: int) -> bool:
        d = str(c)
        e = ""
        for f in range(len(d) - 1, -1, -1):
            e += d[f]
        return d == e

    g = 0  # count of even palindromes
    h = 0  # count of odd palindromes
    i = 1

    while i <= a:
        if i % 2 == 1:
            if b(i):
                h += 1
        else:
            if b(i):
                g += 1
        i += 1

    return g, h