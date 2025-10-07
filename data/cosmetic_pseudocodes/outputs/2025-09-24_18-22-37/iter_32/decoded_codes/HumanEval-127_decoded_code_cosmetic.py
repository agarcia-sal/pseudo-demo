from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number in (0, 1):
            return False
        if number == 2:
            return True
        for idx in range(2, number):
            if number % idx == 0:
                return False
        return True

    a, b = interval1
    c, d = interval2

    left_endpoint = a if a > c else c
    right_endpoint = b if b < d else d
    diff = right_endpoint - left_endpoint

    if not (diff > 0 and is_prime(diff)):
        return "NO"
    return "YES"