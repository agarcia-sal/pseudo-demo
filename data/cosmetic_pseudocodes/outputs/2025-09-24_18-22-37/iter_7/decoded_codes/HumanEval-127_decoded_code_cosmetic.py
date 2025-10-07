from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number in (0, 1):
            return False
        if number == 2:
            return True
        divisor = 2
        while divisor < number:
            if number % divisor == 0:
                return False
            divisor += 1
        return True

    start_val = interval1[0]
    compare_start = interval2[0]
    low_bound = start_val if start_val > compare_start else compare_start

    end_val = interval1[1]
    compare_end = interval2[1]
    high_bound = end_val if end_val < compare_end else compare_end

    diff = high_bound - low_bound

    if diff > 0:
        return "YES" if is_prime(diff) else "NO"
    return "NO"