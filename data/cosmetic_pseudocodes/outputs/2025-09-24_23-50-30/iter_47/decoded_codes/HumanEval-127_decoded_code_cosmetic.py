from typing import Sequence, Union


def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> str:
    def is_prime(n: int) -> bool:
        if n in (0, 1):
            return False
        if n == 2:
            return True
        for j in range(2, n):
            if n % j == 0:
                return False
        return True

    a, b = interval1
    c, d = interval2
    p = max(a, c)
    q = min(b, d)

    diff = q - p
    if diff > 0 and is_prime(diff):
        return "YES"
    return "NO"