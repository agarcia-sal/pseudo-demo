from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:

    def is_prime(alpha: int) -> bool:

        def check_divisor(beta: int, gamma: int) -> bool:
            if gamma >= beta:
                return True
            if alpha % gamma == 0:
                return False
            return check_divisor(beta, gamma + 1)

        if alpha in (0, 1):
            return False
        if alpha == 2:
            return True
        return check_divisor(alpha, 2)

    left_end = interval1[0] if interval1[0] > interval2[0] else interval2[0]
    right_end = interval1[1] if interval1[1] < interval2[1] else interval2[1]
    overlap = right_end - left_end

    if overlap > 0 and is_prime(overlap):
        return "YES"
    return "NO"