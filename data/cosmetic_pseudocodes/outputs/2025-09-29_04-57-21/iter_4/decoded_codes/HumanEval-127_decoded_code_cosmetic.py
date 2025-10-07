from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(candidate: int) -> bool:
        if candidate in (0, 1):
            return False
        if candidate == 2:
            return True
        if candidate % 2 == 0:
            return False
        divisor = 3
        while divisor * divisor <= candidate:
            if candidate % divisor == 0:
                return False
            divisor += 2
        return True

    lower_bound, upper_bound = interval1
    other_lower, other_upper = interval2

    start_point = other_lower if lower_bound < other_lower else lower_bound
    end_point = other_upper if upper_bound > other_upper else upper_bound

    overlap_length = end_point - start_point
    if overlap_length > 0 and is_prime(overlap_length):
        return "YES"
    return "NO"