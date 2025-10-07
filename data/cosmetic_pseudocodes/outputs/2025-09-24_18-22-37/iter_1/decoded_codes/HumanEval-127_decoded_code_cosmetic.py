from typing import Tuple, Union

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        if number <= 1:
            return False
        if number == 2:
            return True
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True

    left_bound: int = interval1[0] if interval1[0] > interval2[0] else interval2[0]
    right_bound: int = interval1[1] if interval1[1] < interval2[1] else interval2[1]
    length: int = right_bound - left_bound

    if length > 0 and is_prime(length):
        return "YES"
    else:
        return "NO"