from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        def check_divisor(divisor: int) -> bool:
            if divisor * divisor > number:
                return True
            if number % divisor == 0:
                return False
            return check_divisor(divisor + 1)

        if number in (0, 1):
            return False
        if number == 2:
            return True
        return check_divisor(2)

    left_endpoint = interval1[0]
    if interval2[0] > left_endpoint:
        left_endpoint = interval2[0]

    right_endpoint = interval1[1]
    if right_endpoint > interval2[1]:
        right_endpoint = interval2[1]

    intersection_length = right_endpoint - left_endpoint

    if intersection_length > 0 and is_prime(intersection_length):
        return "YES"
    return "NO"