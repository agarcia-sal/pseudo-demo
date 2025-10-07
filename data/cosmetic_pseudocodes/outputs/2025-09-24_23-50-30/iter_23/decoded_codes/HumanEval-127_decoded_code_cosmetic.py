from typing import Sequence, Union


def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> str:
    def is_prime(number: int) -> bool:
        if number <= 1:
            return False
        if number == 2:
            return True
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True

    start_point = max(interval1[0], interval2[0])
    end_point = min(interval1[1], interval2[1])
    length_overlap = end_point - start_point

    if length_overlap <= 0 or not is_prime(length_overlap):
        return "NO"
    return "YES"