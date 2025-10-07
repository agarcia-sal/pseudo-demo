from typing import Tuple


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number < 2:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for divisor in range(3, int(number**0.5) + 1, 2):
            if number % divisor == 0:
                return False
        return True

    start_point, end_point = interval1
    start_alt, end_alt = interval2

    left_limit = max(start_point, start_alt)
    right_limit = min(end_point, end_alt)

    diff = right_limit - left_limit

    if diff > 0 and is_prime(diff):
        return "YES"
    return "NO"