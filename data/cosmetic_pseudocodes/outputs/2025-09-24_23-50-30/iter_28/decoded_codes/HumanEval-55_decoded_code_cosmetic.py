from typing import Callable

def fib(omega: int) -> int:
    alpha: int = 0
    beta: int = 1
    gamma: int = 0

    def zeta(param: int) -> int:
        delta: int = 0
        epsilon: int = 1
        eta: int = 0
        theta: int = 2

        while theta <= param:
            eta = delta + epsilon
            delta = epsilon
            epsilon = eta
            theta += 1

        if param <= 0:
            return 0
        elif param == 1:
            return 1
        else:
            return eta

    return zeta(omega)