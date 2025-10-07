from typing import Tuple

def intersection(alpha: Tuple[int, int], beta: Tuple[int, int]) -> str:
    def is_prime(gamma: int) -> bool:
        if gamma in (0, 1):
            return False
        if gamma == 2:
            return True
        for idx in range(2, gamma):
            if gamma % idx == 0:
                return False
        return True

    p, r = alpha
    q, s = beta

    start_bound = max(p, q)
    end_bound = min(r, s)
    diff = end_bound - start_bound

    if diff > 0 and is_prime(diff):
        return "YES"
    return "NO"