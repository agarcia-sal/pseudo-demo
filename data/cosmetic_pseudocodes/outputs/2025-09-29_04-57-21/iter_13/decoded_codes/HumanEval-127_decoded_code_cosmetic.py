from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number < 2:
            return False
        if number == 2:
            return True

        def check_divisor(candidate: int) -> bool:
            if candidate == number:
                return True
            if number % candidate == 0:
                return False
            return check_divisor(candidate + 1)

        return check_divisor(2)

    start_bound, end_bound = interval1
    other_start, other_end = interval2

    overlap_start = other_start if other_start > start_bound else start_bound
    overlap_end = other_end if other_end < end_bound else end_bound

    overlap_length = overlap_end - overlap_start

    if overlap_length <= 0:
        return "NO"
    if not is_prime(overlap_length):
        return "NO"
    return "YES"