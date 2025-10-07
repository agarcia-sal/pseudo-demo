from typing import Tuple, Union

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        for divisor in range(2, n):
            if n % divisor == 0:
                return False
        return True

    start_point: int = interval1[0] if interval1[0] > interval2[0] else interval2[0]
    end_point: int = interval1[1] if interval1[1] < interval2[1] else interval2[1]
    length: int = end_point - start_point
    if length > 0:
        if is_prime(length):
            return "YES"
    return "NO"