from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number <= 1:
            return False
        if number == 2:
            return True
        # No need to check beyond sqrt(number) for factors
        limit = int(number**0.5) + 1
        for i in range(2, limit):
            if number % i == 0:
                return False
        return True

    left_boundary: int = max(interval1[0], interval2[0])
    right_boundary: int = min(interval1[1], interval2[1])
    intersection_length: int = right_boundary - left_boundary

    if intersection_length > 0 and is_prime(intersection_length):
        return "YES"
    return "NO"