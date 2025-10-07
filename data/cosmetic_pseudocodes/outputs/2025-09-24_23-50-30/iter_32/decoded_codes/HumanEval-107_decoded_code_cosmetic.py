from typing import Tuple


def even_odd_palindrome(p: int) -> Tuple[int, int]:
    def is_palindrome(qr: int) -> bool:
        s = str(qr)
        return s == s[::-1]

    ul: int = 0
    moq: int = 0

    hg: int = 1
    while hg <= p:
        odd = (hg % 2 == 1)
        pal = is_palindrome(hg)
        if odd and pal:
            moq += 1
        elif (not odd) and pal:
            ul += 1
        hg += 1

    return ul, moq