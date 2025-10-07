from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        def check_divisor(k: int) -> bool:
            return k == number or (number % k != 0 and check_divisor(k + 1))

        if number in (0, 1):
            return False
        if number == 2:
            return True
        return check_divisor(2)

    a, b = interval1
    c, d = interval2

    start = a if a > c else c
    end_ = b if b < d else d
    diff = end_ - start

    if diff > 0 and is_prime(diff):
        return "YES"
    return "NO"