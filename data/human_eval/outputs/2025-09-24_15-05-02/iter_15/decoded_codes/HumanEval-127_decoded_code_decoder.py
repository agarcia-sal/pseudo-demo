from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number == 0 or number == 1:
            return False
        if number == 2:
            return True
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    left_bound = max(interval1[0], interval2[0])
    right_bound = min(interval1[1], interval2[1])
    intersection_length = right_bound - left_bound

    if intersection_length > 0 and is_prime(intersection_length):
        return "YES"
    else:
        return "NO"