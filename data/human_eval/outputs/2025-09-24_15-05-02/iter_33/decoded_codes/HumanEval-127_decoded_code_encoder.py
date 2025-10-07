from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number <= 1:
            return False
        if number == 2:
            return True
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    left_endpoint: int = max(interval1[0], interval2[0])
    right_endpoint: int = min(interval1[1], interval2[1])
    length_of_intersection: int = right_endpoint - left_endpoint
    if length_of_intersection > 0 and is_prime(length_of_intersection):
        return "YES"
    return "NO"