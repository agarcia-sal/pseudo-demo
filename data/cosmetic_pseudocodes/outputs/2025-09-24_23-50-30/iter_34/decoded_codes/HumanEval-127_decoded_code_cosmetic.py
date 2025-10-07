from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(k: int) -> bool:
        if k == 0 or k == 1:
            return False
        if k == 2:
            return True
        for q in range(2, k):
            if k % q == 0:
                return False
        return True

    a, b = interval1
    c, d = interval2

    s = a if a > c else c
    t = b if b < d else d
    r = t - s

    if r > 0 and is_prime(r):
        return "YES"
    return "NO"