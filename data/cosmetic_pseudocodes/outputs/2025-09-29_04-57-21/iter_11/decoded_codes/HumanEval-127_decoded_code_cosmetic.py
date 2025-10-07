from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number == 0 or number == 1:
            return False
        if number == 2:
            return True
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True

    start_point: int = max(interval1[0], interval2[0])
    end_point: int = min(interval1[1], interval2[1])
    length_overlap: int = end_point - start_point
    if length_overlap > 0 and is_prime(length_overlap):
        return "YES"
    return "NO"