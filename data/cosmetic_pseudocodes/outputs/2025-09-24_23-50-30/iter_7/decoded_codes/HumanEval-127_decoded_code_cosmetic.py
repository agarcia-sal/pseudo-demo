from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(n: int) -> bool:
        if not (n > 2):
            return n == 2

        def check_divisor(d: int, limit: int) -> bool:
            if d == limit:
                return True
            if n % d == 0:
                return False
            return check_divisor(d + 1, limit)

        return check_divisor(2, n - 1)

    a, b = interval1
    c, d = interval2

    low_bound = a if a > c else c
    up_bound = b if b < d else d

    length_intersect = up_bound - low_bound
    if length_intersect > 0 and is_prime(length_intersect):
        return "YES"
    return "NO"