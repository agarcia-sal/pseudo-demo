from typing import Tuple

def intersection(alpha: Tuple[int, int], beta: Tuple[int, int]) -> str:
    def is_prime(gamma: int) -> bool:
        if gamma in (0, 1):
            return False
        if gamma == 2:
            return True

        def recur_divisor_check(delta: int, epsilon: int) -> bool:
            if epsilon > delta - 1:
                return True
            if delta % epsilon == 0:
                return False
            return recur_divisor_check(delta, epsilon + 1)

        return recur_divisor_check(gamma, 2)

    lower_bound = alpha[0] if alpha[0] > beta[0] else beta[0]
    upper_bound = alpha[1] if alpha[1] < beta[1] else beta[1]
    length_intersect = upper_bound - lower_bound

    if not (length_intersect <= 0 or not is_prime(length_intersect)):
        return "YES"
    return "NO"