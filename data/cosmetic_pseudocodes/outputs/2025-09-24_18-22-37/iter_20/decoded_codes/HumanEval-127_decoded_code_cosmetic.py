from typing import Sequence, Union


def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> str:
    def is_prime(number: int) -> bool:
        if number in (0, 1):
            return False
        if number == 2:
            return True
        for counter in range(2, number):
            if number % counter == 0:
                return False
        return True

    start_point = interval1[0]
    second_start = interval2[0]
    left_endpoint = start_point if start_point > second_start else second_start

    end_point1 = interval1[1]
    end_point2 = interval2[1]
    right_endpoint = end_point1 if end_point1 < end_point2 else end_point2

    diff = right_endpoint - left_endpoint
    if diff > 0:
        prime_check = is_prime(diff)
        if prime_check:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"