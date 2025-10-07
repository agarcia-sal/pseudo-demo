from typing import Tuple

def even_odd_palindrome(x: int) -> Tuple[int, int]:
    def is_palindrome(y: int) -> bool:
        p: str = str(y)
        q: str = ""
        r: int = len(p) - 1
        while r >= 0:
            q += p[r]
            r -= 1
        return p == q

    count_e: int = 0
    count_o: int = 0

    j: int = 1
    while j <= x:
        if j % 2 != 0:
            if is_palindrome(j):
                count_o += 1
        else:
            if is_palindrome(j):
                count_e += 1
        j += 1

    return count_e, count_o