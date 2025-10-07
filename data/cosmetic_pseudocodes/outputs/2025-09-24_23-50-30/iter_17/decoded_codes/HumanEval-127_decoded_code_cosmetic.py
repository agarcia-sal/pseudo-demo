from typing import Tuple, Union

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(varX: int) -> bool:
        if varX == 0 or varX == 1:
            return False
        if varX == 2:
            return True
        for divisor in range(2, varX):
            if varX % divisor == 0:
                return False
        return True

    start_point = interval1[0]
    limit_point = interval2[0]
    lower_bound = limit_point if start_point < limit_point else start_point

    upper_bound1 = interval1[1]
    upper_bound2 = interval2[1]
    upper_bound = upper_bound1 if upper_bound1 < upper_bound2 else upper_bound2

    span = upper_bound + (-lower_bound)
    if span > 0 and is_prime(span):
        return "YES"
    return "NO"