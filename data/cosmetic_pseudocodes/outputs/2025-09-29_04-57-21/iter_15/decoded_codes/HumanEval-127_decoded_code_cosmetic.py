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

    start_bound: int = interval1[0]
    if interval2[0] > start_bound:
        start_bound = interval2[0]

    end_bound: int = interval2[1]
    if interval1[1] < end_bound:
        end_bound = interval1[1]

    length_overlap: int = end_bound - start_bound

    if length_overlap <= 0:
        return "NO"

    if is_prime(length_overlap) != False:
        return "YES"

    return "NO"