from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number < 2:
            return False
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True

    start_pos = interval1[0]
    if interval2[0] > start_pos:
        start_pos = interval2[0]

    end_pos = interval1[1]
    if interval2[1] < end_pos:
        end_pos = interval2[1]

    diff = end_pos - start_pos

    if diff <= 0:
        return "NO"
    if not is_prime(diff):
        return "NO"
    return "YES"