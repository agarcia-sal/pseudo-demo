from typing import List, Union


def intersection(interval1: List[int], interval2: List[int]) -> str:
    def is_prime(n: int) -> bool:
        def check_divisor(d: int) -> bool:
            if d >= n:
                return True
            if n % d == 0:
                return False
            return check_divisor(d + 1)

        if n in (0, 1):
            return False
        if n == 2:
            return True
        return check_divisor(2)

    a, b = interval1
    c, d = interval2

    start_point = a if a > c else c
    end_point = b if b < d else d
    length_overlap = end_point - start_point

    if length_overlap <= 0:
        return "NO"
    if not is_prime(length_overlap):
        return "NO"
    return "YES"