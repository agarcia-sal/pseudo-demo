from typing import Tuple, Union

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(n: int) -> bool:
        if not (n > 2):
            if n == 2:
                return True
            return False

        def check_divisor(d: int) -> bool:
            if d * d > n:
                return True
            if n % d == 0:
                return False
            return check_divisor(d + 1)

        return check_divisor(2)

    a, b = interval1
    c, d = interval2

    low_bound = a if a > c else c
    high_bound = b if b < d else d
    diff = high_bound - low_bound

    if not (diff <= 0 or not is_prime(diff)):
        return "YES"
    else:
        return "NO"