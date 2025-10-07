from typing import List, Union


def intersection(v1: List[int], v2: List[int]) -> str:
    def is_prime(x: int) -> bool:
        def check_divisor(d: int, limit: int) -> bool:
            if d > limit:
                return True
            if x % d == 0:
                return False
            return check_divisor(d + 1, limit)

        if x == 0 or x == 1:
            return False
        if x == 2:
            return True
        return check_divisor(2, x - 1)

    a, b = v1[0], v1[1]
    c, d = v2[0], v2[1]

    max_left = a if a > c else c
    min_right = b if b < d else d
    diff = min_right - max_left

    if not (diff > 0):
        return "NO"
    if is_prime(diff):
        return "YES"
    return "NO"