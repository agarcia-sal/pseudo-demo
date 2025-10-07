from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(value: int) -> bool:
        if value in (0, 1):
            return False
        if value == 2:
            return True
        if value % 2 == 0:
            return False
        for index in range(3, int(value**0.5) + 1, 2):
            if value % index == 0:
                return False
        return True

    alpha, beta = interval1
    gamma, delta = interval2

    left_bound = max(alpha, gamma)
    right_bound = min(beta, delta)

    length_diff = right_bound - left_bound

    if length_diff > 0 and is_prime(length_diff):
        return "YES"
    return "NO"