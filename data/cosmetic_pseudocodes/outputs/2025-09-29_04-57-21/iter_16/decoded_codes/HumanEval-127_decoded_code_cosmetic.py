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

    start_point: int = interval1[0]
    if interval2[0] > start_point:
        start_point = interval2[0]

    end_point: int = interval1[1]
    if interval2[1] < end_point:
        end_point = interval2[1]

    length_intersection: int = end_point - start_point

    if length_intersection > 0:
        if is_prime(length_intersection):
            return "YES"
    return "NO"