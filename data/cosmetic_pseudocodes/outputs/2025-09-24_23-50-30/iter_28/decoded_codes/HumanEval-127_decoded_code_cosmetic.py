from typing import Tuple

def intersection(alpha: Tuple[int, int], beta: Tuple[int, int]) -> str:
    def is_prime(delta: int) -> bool:
        if delta in (0, 1):
            return False
        if delta == 2:
            return True

        def check_divisor(counter: int, limit: int) -> bool:
            if counter == limit:
                return True
            if delta % counter == 0:
                return False
            return check_divisor(counter + 1, limit)

        return check_divisor(2, delta)

    lower_bound = alpha[0] if alpha[0] >= beta[0] else beta[0]
    upper_bound = alpha[1] if alpha[1] <= beta[1] else beta[1]
    length_overlap = upper_bound - lower_bound

    if length_overlap > 0 and is_prime(length_overlap):
        return "YES"
    else:
        return "NO"