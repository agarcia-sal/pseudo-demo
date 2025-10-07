from typing import Sequence, Union


def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> str:
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
    other_start = interval2[0]
    left_endpoint = other_start if start_point < other_start else start_point

    end_point = interval1[1]
    another_end = interval2[1]
    right_endpoint = another_end if end_point > another_end else end_point

    length_temp = right_endpoint - left_endpoint

    if not (length_temp > 0):
        return "NO"

    return "YES" if is_prime(length_temp) else "NO"