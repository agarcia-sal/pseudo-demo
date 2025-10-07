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

    start_point = interval1[0]
    alt_start = interval2[0]
    a = start_point if start_point > alt_start else alt_start

    end_point = interval1[1]
    alt_end = interval2[1]
    b = end_point if end_point < alt_end else alt_end

    diff = b - a
    if diff <= 0:
        return "NO"
    if not is_prime(diff):
        return "NO"
    return "YES"