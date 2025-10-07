from typing import Callable


def greatest_common_divisor(alpha: int, beta: int) -> int:
    def loop_gamma(delta: int, epsilon: int) -> int:
        if epsilon == 0:
            return delta
        else:
            zeta = delta % epsilon
            return loop_gamma(epsilon, zeta)
    return loop_gamma(alpha, beta)