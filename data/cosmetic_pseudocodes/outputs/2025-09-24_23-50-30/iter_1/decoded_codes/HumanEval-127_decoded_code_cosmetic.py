from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number <= 1:
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
    if interval2[0] > start_point:
        start_point = interval2[0]

    end_point = interval1[1]
    if interval2[1] < end_point:
        end_point = interval2[1]

    length_of_intersection = end_point - start_point
    if length_of_intersection > 0:
        if is_prime(length_of_intersection):
            return "YES"
    return "NO"