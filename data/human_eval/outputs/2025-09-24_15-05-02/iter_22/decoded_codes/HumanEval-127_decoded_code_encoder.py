from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number in (0, 1):
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for divisor in range(3, int(number ** 0.5) + 1, 2):
            if number % divisor == 0:
                return False
        return True

    left_bound: int = max(interval1[0], interval2[0])
    right_bound: int = min(interval1[1], interval2[1])
    intersection_length: int = right_bound - left_bound

    if intersection_length > 0 and is_prime(intersection_length):
        return "YES"
    return "NO"