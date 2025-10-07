from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number < 2:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

    left_boundary: int = max(interval1[0], interval2[0])
    right_boundary: int = min(interval1[1], interval2[1])
    length: int = right_boundary - left_boundary

    if length > 0 and is_prime(length):
        return "YES"
    return "NO"