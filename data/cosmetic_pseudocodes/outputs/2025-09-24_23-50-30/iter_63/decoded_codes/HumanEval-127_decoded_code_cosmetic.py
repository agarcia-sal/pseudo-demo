from typing import Tuple, Union

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(alpha: int) -> bool:
        if alpha == 0 or alpha == 1:
            return False
        if alpha == 2:
            return True

        def check_divisible(beta: int, divisor: int) -> bool:
            if divisor == beta:
                return True
            if beta % divisor == 0:
                return False
            return check_divisible(beta, divisor + 1)

        return check_divisible(alpha, 2)

    start_point = max(interval1[0], interval2[0])
    end_point = min(interval1[1], interval2[1])
    gap_length = end_point - start_point

    if gap_length > 0 and is_prime(gap_length):
        return "YES"
    return "NO"