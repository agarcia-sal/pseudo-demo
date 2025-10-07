from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(num: int) -> bool:
        if num <= 1:
            return False
        if num == 2:
            return True
        # Check divisibility up to sqrt(num) for efficiency
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                return False
        return True

    start_val, end_val = interval1
    alpha, beta = interval2

    left_bound = start_val if start_val > alpha else alpha
    right_bound = end_val if end_val < beta else beta
    diff = right_bound - left_bound

    if diff > 0 and is_prime(diff):
        return "YES"
    return "NO"