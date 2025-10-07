from math import floor, sqrt
from typing import List


def prime_fib(alpha: int) -> int:
    def is_prime(beta: int) -> bool:
        if beta < 2:
            return False
        upper_limit = min(floor(sqrt(beta)) + 1, beta - 1)
        for gamma in range(2, upper_limit):
            if beta % gamma == 0:
                return False
        return True

    delta: List[int] = [0, 1]

    def loop_epsilon(epsilon: List[int], zeta: int) -> int:
        if zeta == 0:
            return epsilon[-1]
        eta = epsilon[-1] + epsilon[-2]
        epsilon.append(eta)
        if is_prime(eta):
            zeta -= 1
        return loop_epsilon(epsilon, zeta)

    return loop_epsilon(delta, alpha)