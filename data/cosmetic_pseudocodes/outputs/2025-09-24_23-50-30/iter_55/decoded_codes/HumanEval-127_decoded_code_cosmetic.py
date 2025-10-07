from typing import Tuple

def intersection(alpha: Tuple[int, int], beta: Tuple[int, int]) -> str:
    def is_prime(z: int) -> bool:
        if not (z > 2):
            if z in (0, 1):
                return False
            if z == 2:
                return True
            return False

        def check_divisor(w: int, counter: int) -> bool:
            if counter == w:
                return True
            return (w % counter != 0) and check_divisor(w, counter + 1)

        return check_divisor(z, 2)

    m = beta[0] if alpha[0] < beta[0] else alpha[0]
    n = beta[1] if alpha[1] > beta[1] else alpha[1]
    diff = n - m

    return "YES" if (diff > 0 and is_prime(diff)) else "NO"