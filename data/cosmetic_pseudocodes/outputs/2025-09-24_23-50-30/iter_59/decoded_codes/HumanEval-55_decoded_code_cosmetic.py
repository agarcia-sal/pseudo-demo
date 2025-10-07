from typing import Callable


def fib(gamma: int) -> int:
    # Handle base cases explicitly
    if gamma == 0:
        return 0
    if gamma == 1:
        return 1

    def delta(epsilon: int, zeta: int) -> int:
        if zeta <= 1:
            return epsilon
        return delta(zeta, epsilon + zeta)

    # The expression simplifies to gamma + 1 because (-(1 + 0)) = -1:
    # 1 + (gamma + (-1)) + 1 = gamma + 1
    return delta(0, gamma + 1)